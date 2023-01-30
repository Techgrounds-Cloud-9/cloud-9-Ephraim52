import boto3
import project_final.certmaker_stack as certmaker_stack
from os.path import exists

def generate_certificate():
    if exists("arn.txt"):
        f = open("arn.txt", "r+")
        return f.read()
    else:
        acm = boto3.client("acm")
        response = acm.import_certificate(
            Certificate=certmaker_stack.certifictate_pem,
            PrivateKey=certmaker_stack.private_key_pem,
            CertificateChain=certmaker_stack.ca_certifictate_pem,
        )
        arn = response["CertificateArn"]
        f = open("arn.txt", "w+")
        f.write(arn)
        return arn