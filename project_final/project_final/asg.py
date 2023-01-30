from aws_cdk import(
    Stack,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_kms as kms,
    aws_autoscaling as autoscaling,
    Duration,
    aws_iam as iam,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as acm,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
)

import aws_cdk as cdk

from constructs import Construct

import os

# webserver_sg: ec2.SecurityGroup,
# security group, vpc and role need to be connected to the main Stack in order to work and to provide the userdata
class web_asg_alb(Stack):

    def __init__(self, scope: Construct, construct_id: str, webserver_encryption_key: kms.Key, rick_rolled: iam.Role, vpc_asg: ec2.Vpc, certificate:acm.Certificate, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create request to provide userdata for the asg

        ###### Webserver Security Group ######
        WebSG = ec2.SecurityGroup(self, 'Web SG',
        vpc= vpc_asg,
        allow_all_outbound=True,
        description= 'webserver security group'
        )
        # self.websecurity=WebSG

        WebSG.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.10.10.0/24"),
            connection=ec2.Port.tcp(80),
            description='allow HTTP from anywhere'
        )

        # WebSG.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(),
        #     connection=ec2.Port.tcp(443),
        #     description='allow HTTPS from anywhere'
        # )

        WebSG.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.20.20.0/24"),
            connection=ec2.Port.tcp(22),
            description='Allow SSH traffic from the Admin server'
        )

        # AutoSC_SG= ec2.SecurityGroup(self, 'autoscaling group security',
        #     vpc=vpc_asg,
        #     allow_all_outbound=True,
        #     description='Security group for asg'
        # )
        
        # AutoSC_SG.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(),
        #     connection=ec2.Port.tcp(80),
        #     description='allow HTTP from anywhere',
        # )

        # AutoSC_SG.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(),
        #     connection=ec2.Port.tcp(443),
        #     description='allow HTTPS from anywhere',
        # )

        ###### KMS key for AMI ######
        Webserver_KeyPair = ec2.CfnKeyPair(self, "Webserver_KeyPair",
            key_name = "webserver_key",
            )

        ###### Provide launch template ######
        web_launch_template=ec2.LaunchTemplate(
            self, 'Web_template_for_launch',
            launch_template_name="web_launch_template",
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            user_data= ec2.UserData.for_linux(),
            key_name=Webserver_KeyPair.key_name,
            role=rick_rolled,
            security_group=WebSG,
            block_devices=[
                ec2.BlockDevice(
                    device_name='/dev/xvda',
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        # kms_key=webserver_encryption_key,
                        delete_on_termination=True,
                        ))],
        )

        ###### Configure & Create ASG ######
        web_autoscaling=autoscaling.AutoScalingGroup(
            self, 'web-autoscaling-group',
            vpc=vpc_asg,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
            launch_template=web_launch_template,
            min_capacity=1,
            max_capacity=3,
        )

        ###### Scaling Policy ######
        web_autoscaling.scale_on_cpu_utilization(
            "cpu-auto-scaling",
            target_utilization_percent=80,
        )

        ###### S3 Bucket creation ######
        script_bucket = s3.Bucket(
            self, construct_id,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            enforce_ssl=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        ###### Uploading the Userdata to the bucket ######
        self.deployment = s3deploy.BucketDeployment(
            self, 'Script Bucket Deployment',
            destination_bucket=script_bucket,
            sources=[s3deploy.Source.asset(os.path.join("./Bucket"))]
        )

        ###### Role for EC2 instances access Userdata ######
        script_bucket.add_to_resource_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                principals=[iam.ServicePrincipal('ec2.amazonaws.com')],
                actions=['s3:GetObject'],
                resources=[f'{script_bucket.bucket_arn}/*'])
        )

        ###### Download webserver Userdata script ######
        script_path = web_launch_template.user_data.add_s3_download_command(
            bucket= script_bucket,
            bucket_key='userdata1.sh',
        )

        web_launch_template.user_data.add_execute_file_command(file_path=script_path)

        ###### Create Load Balancer ######
        alb=elbv2.ApplicationLoadBalancer(
            self, 'Webserver LoadBalancer',
            vpc=vpc_asg,
            internet_facing=True,
        )

        ###### Redirect HTTP to HTTPS ######
        alb.add_redirect()

        # ###### In between the certificate should be called in ######
        # arn="arn:aws:acm:eu-central-1:712170961429:certificate/input_certcode"

        # ###### Call the certificate ######
        # certificate=acm.Certificate.from_certificate_arn(self, "Certificate", arn)

        ###### Used to call the ALB DNS ######
        # dns = apLb.load_balancer_dns_name

        ###### Listener for HTTPS ######
        listener= alb.add_listener(
            'listener for HTTP',
            port=443,
            open=True,
            ssl_policy=elbv2.SslPolicy.FORWARD_SECRECY_TLS12,
            certificates=[certificate],
        )

        ###### Target group HTTP ######
        target_group=listener.add_targets(
            'asg target group',
            port=80,
            targets=[web_autoscaling],
            health_check=elbv2.HealthCheck(
                enabled=True,
                interval=Duration.seconds(5),
                protocol = elbv2.Protocol.HTTP,
                port='80',
                timeout= Duration.seconds(2),
                path="/",
            ),
            # stickiness_cookie_duration=Duration.minutes(5),
            # stickiness_cookie_name="public cookie",
        )