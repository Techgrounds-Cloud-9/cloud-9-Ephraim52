## Demands of the application by the productowner

- All VM's have to be encrypted
- The webserver has to have a daily created backup, this backup has to be stored for 7 days.
- The webserver has to be installed by an automated process
- The admin/management has to be available through the public IP
- The admin/management server should only be accessible from reliable trustworthy locations
- These IP ranges are available for usage 10.10.10.0/24 & 10.20.20.0/24
- All subnets have to be protected by a firewall on the subnet level
- SSH or RDP connections with the webserver are only allowed from the admin server
- Improve the architecture where needed and keep it real in order to meet the deadline

## Assumed demands of the application for the architecture

Infrastructure
- VPC - Region
- Public & Private subnets - Availability Zones, the IP ranges are set for the subnets
- NAT gateway - Attached to the Private Subnet for connection with the internet
- Internet Gateway - Attached to the Public Subnet for connection with the internet
- ACL's as firewall on subnet level
- Security group as firewall on the instance level
- Create a Function with Lambda to create snapshots daily and store/save for 7 days, AWS EC2 Backup
- Two instances in 2 different availability zones to set up the admin/management servers individually
- Add KMS - for encrypting and decrypting the VM's
- EC2 instances attached to the VPC with potentially if extra space is needed EBS volumes too
- S3 storage

IAM
- assign roles to services
- least privilege
- rotate keys regularely - KMS
