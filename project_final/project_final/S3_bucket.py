from aws_cdk import (
    Duration,
    RemovalPolicy,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_iam as iam,
)

import aws_cdk as cdk

from constructs import Construct

import os

class S3bucket(Construct):

    def __init__(self, scope: Construct, construct_id: str, resource_access, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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

        # Can be added to the userdata script and attach it to the admin server to automate SSH connection.
        # amazon.ec2.windows
        # "<powershell>",
        #     "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0",
        #     "Start-Service ssh-agent",
        #     "Start-Service sshd"
        # ssh -J <Administrator@adminserver> -I <key> -I <key> <ec2-user@webserver>