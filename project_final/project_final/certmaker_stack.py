import random
import boto3
import time
from aws_cdk import(
    Stack, 
    aws_certificatemanager as acm,
    )

from OpenSSL import crypto

from constructs import Construct

class CertStack(Stack):
    httpscertificate=acm.Certificate
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        # Create CA
        ca_key = crypto.PKey()
        ca_key.generate_key(crypto.TYPE_RSA, 2048)
        ca_cert = crypto.X509()
        ca_cert.set_version(2)
        ca_cert.set_serial_number(random.randrange(100000))
        ca_subj = ca_cert.get_subject()
        ca_subj.C = "NL"
        ca_subj.ST = "Noord-Holland"
        ca_subj.L = "Amsterdam"
        ca_subj.O = "MyOrganization"
        ca_subj.OU = "MyOrganizationalUnit"
        ca_subj.CN = "Dominic"
        ca_cert.add_extensions([
            crypto.X509Extension(b"subjectKeyIdentifier", False, b"hash", subject=ca_cert),
        ])
        ca_cert.add_extensions([
            crypto.X509Extension(b"authorityKeyIdentifier", False, b"keyid:always", issuer=ca_cert),
        ])
        ca_cert.add_extensions([
            crypto.X509Extension(b"basicConstraints", False, b"CA:TRUE"),
            crypto.X509Extension(b"keyUsage", False, b"keyCertSign, cRLSign"),
        ])
        ca_cert.set_issuer(ca_subj)
        ca_cert.set_pubkey(ca_key)
        ca_cert.sign(ca_key, 'sha256')
        ca_cert.gmtime_adj_notBefore(0)
        ca_cert.gmtime_adj_notAfter(10*365*24*60*60)
        ca_certifictate_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, ca_cert).decode('utf-8')

        # Create Self-Signed Certificate
        client_key = crypto.PKey()
        client_key.generate_key(crypto.TYPE_RSA, 2048)
        client_cert = crypto.X509()
        client_cert.set_version(2)
        client_cert.set_serial_number(random.randrange(100000))
        client_subj = client_cert.get_subject()
        client_subj.C = "NL"
        client_subj.ST = "Noord-Holland"
        client_subj.L = "Amsterdam"
        client_subj.O = "MyOrganization"
        client_subj.OU = "MyOrganizationalUnit"
        client_subj.CN = "Dominic"
        client_cert.add_extensions([
            crypto.X509Extension(b"basicConstraints", False, b"CA:FALSE"),
            crypto.X509Extension(b"subjectKeyIdentifier", False, b"hash", subject=client_cert),
        ])
        client_cert.add_extensions([
            crypto.X509Extension(b"authorityKeyIdentifier", False, b"keyid:always", issuer=ca_cert),
            crypto.X509Extension(b"extendedKeyUsage", False, b"serverAuth"),
            crypto.X509Extension(b"keyUsage", False, b"digitalSignature"),
        ])
        client_cert.add_extensions([
            crypto.X509Extension(b'subjectAltName', False,
                ','.join([
                    'DNS:*createyourownwebsite.com'
        ]).encode())])
        client_cert.set_issuer(ca_subj)
        client_cert.set_pubkey(client_key)
        client_cert.gmtime_adj_notBefore(0)
        client_cert.gmtime_adj_notAfter(9*365*24*60*60)
        client_cert.sign(ca_key, 'sha256')
        certifictate_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, client_cert).decode('utf-8')
        private_key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, client_key).decode('utf-8')
        response = {
            'certificate': certifictate_pem,
            'private_key': private_key_pem,
            'certificate_chain': ca_certifictate_pem
        }
        time.sleep(2)
        acmboto3 = boto3.client("acm")
        response = acmboto3.import_certificate(
            Certificate=certifictate_pem,
            PrivateKey=private_key_pem,
            CertificateChain=ca_certifictate_pem,
        )
        arn = response["CertificateArn"]
        domcertified=acm.Certificate.from_certificate_arn(
            self, "whatever",
            certificate_arn=arn,
            )
        self.httpscertificate=domcertified