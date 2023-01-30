from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)

from constructs import Construct

class NACL_Stack(Stack):
# vpc's need to be added into this definition
    def __init__(self, scope: Construct, construct_id: str, vpc_asg: ec2.Vpc, mng_vpc: ec2.Vpc, **kwargs ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ###### My trusted IP Address ######
        my_ip = "83.81.114.11/32"

        ###### Create Nacl for the Web VPC ######
        web_network_acl = ec2.NetworkAcl(
            self, 'private Web VPC Acl',
            vpc=vpc_asg,
            network_acl_name='Web VPC Acl',
            subnet_selection=ec2.SubnetSelection(
                subnet_type= ec2.SubnetType.PRIVATE_WITH_EGRESS
            )
        )

        ###### Rules for the Web VPC Acl ######
        web_network_acl.add_entry(
            'HTTP inbound allow',
            cidr=ec2.AclCidr.ipv4(vpc_asg.vpc_cidr_block),
            rule_number= 100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'HTTP outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number= 100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'HTTPS inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number= 110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'HTTP-outbound-allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number= 110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'SSH inbound allow',
            cidr=ec2.AclCidr.ipv4(mng_vpc.vpc_cidr_block),
            rule_number= 120,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'SSH Ephemeral outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number= 120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'Ephemeral HTTP inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number= 130,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'Ephemeral to HTTPS outbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=130,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'Ephemeral ipv6 inbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'HTTPS outbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=150,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_network_acl.add_entry(
            'Ephemeral outbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=160,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        ###### Create Nacl for the private subnet ######
        alb_nacl=ec2.NetworkAcl(
            self, 'public load balancer webserver acl',
            vpc=vpc_asg,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        ###### Rules for the WebVPC private subnet ######
        alb_nacl.add_entry(
            'HTTP inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        alb_nacl.add_entry(
            'HTTP outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        alb_nacl.add_entry(
            'HTTPS inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=310,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        alb_nacl.add_entry(
            'HTTPS outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=310,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        alb_nacl.add_entry(
            'Ephemeral inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=320,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        alb_nacl.add_entry(
            'Ephemeral outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=320,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        alb_nacl.add_entry(
            'Ephemeral ipv6 inbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=330,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        alb_nacl.add_entry(
            'Ephemeral ipv6 outbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=330,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        # Redirect incoming HTTP traffic to HTTPS
        alb_nacl.add_entry(
            'HTTP ipv6 inbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=340,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        alb_nacl.add_entry(
            'HTTPS ipv6 inbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=350,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        ###### Create Nacl for the Admin VPC ######
        admin_network_acl = ec2.NetworkAcl(
            self, 'Admin VPC Acl',
            vpc= mng_vpc,
            network_acl_name='Admin VPC Acl',
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        ###### Rules for the Admin VPC Acl ######
        admin_network_acl.add_entry(
            'SSH home inbound allow',
            cidr=ec2.AclCidr.ipv4(my_ip),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'SSH web outbound allow',
            cidr=ec2.AclCidr.ipv4(vpc_asg.vpc_cidr_block),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'RDP inbound allow',
            cidr=ec2.AclCidr.ipv4(my_ip),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'RDP outbound allow',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'Ephemeral ipv4 inbound web',
            cidr=ec2.AclCidr.ipv4(vpc_asg.vpc_cidr_block),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'HTTPS ipv6 outbound web',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'Ephemeral ipv6 inbound allow trusted ip',
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=150,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'Ephemeral ipv4 outbound trusted ip',
            cidr=ec2.AclCidr.ipv4(my_ip),
            rule_number=150,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'Ephemeral ipv4 inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=160,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'HTTP outbound web',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=160,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_network_acl.add_entry(
            'HTTPS outbound web',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=170,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )