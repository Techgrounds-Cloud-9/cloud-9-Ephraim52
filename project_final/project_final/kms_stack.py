from aws_cdk import (
    Stack,
    aws_kms as kms,
    RemovalPolicy
)
from constructs import Construct

class KMS_stack(Stack):
    admin_key = kms.Key
    web_key = kms.Key
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Admin_Key = kms.Key(self, "Admin_Key",
            enable_key_rotation = True,
            alias = "Admin_Key",
            removal_policy = RemovalPolicy.DESTROY)
        self.admin_key = Admin_Key

        Web_Key = kms.Key(self, "Web_Key",
            enable_key_rotation = True,
            alias = "Web_Key",
            removal_policy = RemovalPolicy.DESTROY)
        self.web_key = Web_Key
