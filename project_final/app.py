#!/usr/bin/env python3
import os

import aws_cdk as cdk

# from project_final.backupvaults import Backup_Construct
from project_final.kms_stack import KMS_stack
from project_final.asg import web_asg_alb
from project_final.nacls import NACL_Stack
from project_final.vpc import VPCStack
from project_final.certmaker_stack import CertStack

app = cdk.App()

needsomecerts= CertStack(app, "MyCertificate")

resource_encryption_Stack = KMS_stack(app, "kmsstack")

VPCStack_ = VPCStack(app, "vpcstack",
    # webserver_encryption_key=resource_encryption_Stack.web_key,
    admin_server_enc_key=resource_encryption_Stack.admin_key,
    )

naclstack = NACL_Stack(app, "NaclStack",
    vpc_asg=VPCStack_.asg_vpc,
    mng_vpc=VPCStack_.vpc_admin,
    )

asg_alb_stack = web_asg_alb(app, "webasgalbstack",
    vpc_asg=VPCStack_.asg_vpc,
    # webserver_sg=VPCStack_.websecurity,
    rick_rolled=VPCStack_.Web_role,
    webserver_encryption_key=resource_encryption_Stack.web_key,
    certificate=needsomecerts.httpscertificate,
    )

# backup_ = Backup_Construct(app, "Backmeup", instances=VPCStack_.webserver)



app.synth()
