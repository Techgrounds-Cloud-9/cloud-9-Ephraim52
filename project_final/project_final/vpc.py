from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_kms as kms,
)

# use letsencrypt certificate for the load balancer 

import aws_cdk as cdk

from constructs import Construct

import os

# webserver_encryption_key: kms.Key,

class VPCStack(Stack):
    asg_vpc = ec2.Vpc
    vpc_admin = ec2.Vpc
    # websecurity = ec2.SecurityGroup
    Web_role = iam.Role
    webserver = ec2.Instance
    def __init__(self, scope: Construct, construct_id: str, admin_server_enc_key: kms.Key, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ###### VPC's ######
        WebVPC = ec2.Vpc(
                self, "Webserver VPC",
                cidr="10.10.10.0/24",
                max_azs=3,
                # availability_zones=["eu-west-2a", "eu-west-2b"],
                nat_gateways=1,
                subnet_configuration=[
                    ec2.SubnetConfiguration(name="public", cidr_mask=28, subnet_type=ec2.SubnetType.PUBLIC),
                    ec2.SubnetConfiguration(name="private", cidr_mask=26, subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
                ]
            )
        self.asg_vpc = WebVPC

        AdminVPC = ec2.Vpc(
                self, "Admin VPC",
                cidr="10.20.20.0/24",
                max_azs=2,
                # availability_zones=["eu-west-2a"],
                nat_gateways=0,
                subnet_configuration=[
                    ec2.SubnetConfiguration(name="public", cidr_mask=25, subnet_type=ec2.SubnetType.PUBLIC)
                    # ec2.SubnetConfiguration(name="private", cidr_mask=25, subnet_type=ec2.SubnetType.PRIVATE)
                ]
            )
        self.vpc_admin = AdminVPC

        ###### Peering Connection ######
        cfn_VPCPeering_connection =ec2.CfnVPCPeeringConnection(self, "VPC peering connection",
            peer_vpc_id = AdminVPC.vpc_id,
            vpc_id = WebVPC.vpc_id,

            # the properties below are optional
            peer_region='eu-central-1',
            )

        # Update Route Tables for Peering Connection
        # From the web vpc to the admin vpc through the route table
        i=0
        for subnet in WebVPC.private_subnets:
            i+=1
            self.webvpc_to_adminvpc_route=ec2.CfnRoute(
                self,
                "WebVPC_to_AdminVPC_Route" + str(i),
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block=AdminVPC.vpc_cidr_block,
                vpc_peering_connection_id=cfn_VPCPeering_connection.attr_id,
            )

        # From the admin vpc to the web vpc through the route table
        j=0
        for subnet in AdminVPC.public_subnets:
            j+=1
            self.adminvpc_to_webvpc_route=ec2.CfnRoute(
                self,
                "AdminVPC_to_WebVPC_Route" + str(j),
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block=WebVPC.vpc_cidr_block,
                vpc_peering_connection_id=cfn_VPCPeering_connection.attr_id,
            )

        ###### Webserver Security Group ######
        # WebSG = ec2.SecurityGroup(self, 'Web SG',
        # vpc= WebVPC,
        # allow_all_outbound=True,
        # description= 'webserver security group'
        # )
        # self.websecurity=WebSG

        # WebSG.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(),
        #     connection=ec2.Port.tcp(80),
        #     description='HTTP'
        # )

        # WebSG.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(),
        #     connection=ec2.Port.tcp(443),
        #     description='HTTPS'
        # )

        # WebSG.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("10.20.20.0/24"),
        #     connection=ec2.Port.tcp(22),
        #     description='Allow SSH traffic from the Admin server'
        # )

        ###### Linking Key Pair ######
        Admin_server_KeyPair = ec2.CfnKeyPair(self, "Admin_server_KeyPair",
            key_name = "admin_key",
            )

        ###### Trusted IP address ######
        my_ip = "83.81.114.11/32"

        ###### Admin server Security Group ######
        AdminSG = ec2.SecurityGroup(self, 'Admin SG',
            vpc= AdminVPC,
            allow_all_outbound = True,
            description = 'AdminSecurityGroup'
        )
        self.admin_sg=AdminSG

        AdminSG.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            connection=ec2.Port.tcp(22),
            description='SSH from trusted location'
        )    

        AdminSG.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            connection=ec2.Port.tcp(3389),
            description='RDP from trusted location'
        )

        ###### Admin server ######
        Instance_Admin_server = ec2.Instance(
            self, 'Admin Server',
            vpc=AdminVPC,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC,),
            security_group= AdminSG,
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            key_name='admin_key',
            block_devices=[
                ec2.BlockDevice(
                device_name='/dev/xvda',
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,
                    encrypted=True,
                    kms_key=admin_server_enc_key,
                    delete_on_termination=True, 
                    ))],
        )

        # WebServer Role for S3 read access
        Web_iam_role = iam.Role(
            self, 'webserver-role',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
                ],
        )
        self.Web_role = Web_iam_role

        ###### Webserver ###### V1.0
        # Instance_Webserver = ec2.Instance(
        #     self, 'Webserver',
        #     vpc=WebVPC,
        #     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC,),
        #     role=Web_iam_role,
        #     security_group=WebSG,
        #     instance_type=ec2.InstanceType('t2.micro'),
        #     machine_image=ec2.MachineImage.latest_amazon_linux(
        #         generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
        #     ),
        #     key_name='webserver_key',
        #     block_devices=[
        #         ec2.BlockDevice(
        #             device_name='/dev/xvda',
        #             volume=ec2.BlockDeviceVolume.ebs(
        #                 volume_size=8,
        #                 encrypted=True,
        #                 kms_key=webserver_encryption_key,
        #                 delete_on_termination=True, 
        #                 ))],
        # )
        # self.webserver = Instance_Webserver

        ###### S3 Bucket creation ###### V1.0
        # script_bucket = s3.Bucket(
        #     self, construct_id,
        #     encryption=s3.BucketEncryption.S3_MANAGED,
        #     versioned=True,
        #     enforce_ssl=True,
        #     removal_policy=cdk.RemovalPolicy.DESTROY,
        #     auto_delete_objects=True,
        # )

        ###### Uploading the Userdata to the bucket ######
        # self.deployment = s3deploy.BucketDeployment(
        #     self, 'Script Bucket Deployment',
        #     destination_bucket=script_bucket,
        #     sources=[s3deploy.Source.asset(os.path.join("./Bucket"))]
        # )

        # ###### Role for EC2 instances access Userdata ######
        # script_bucket.add_to_resource_policy(
        #     iam.PolicyStatement(
        #         effect=iam.Effect.ALLOW,
        #         principals=[iam.ServicePrincipal('ec2.amazonaws.com')],
        #         actions=['s3:GetObject'],
        #         resources=[f'{script_bucket.bucket_arn}/*'])
        # )

        # ###### Download webserver Userdata script ######
        # script_path = Instance_Webserver.user_data.add_s3_download_command(
        #     bucket= script_bucket,
        #     bucket_key='userdata1.sh',
        # )

        # Instance_Webserver.user_data.add_execute_file_command(file_path=script_path)
