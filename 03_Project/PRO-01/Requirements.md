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
- Internet Gateway - Attached to the Public Subnet for connection with the internet
- ACL's as firewall on subnet level
- Security group as firewall on the instance level
- Create plans to ensure that S3 creates Backups on a daily basis and that these are saved for 7 days
- Two instances in 2 different availability zones to set up the admin server and webserver individually
- AMI is needed to setup the EC2 instance as a launch template
- Add KMS - for encrypting and decrypting the data
- EC2 instances attached to the VPC to ensure it runs and has the right access
- S3 storage for Bootstrap scripts to give it userdata when the instance is deployed. This will give shape to the instance when being looked at by the public

IAM
- assign roles to services
- least privilege
- rotate keys regularely - KMS
- Use the SSH keys for encrypting data through KMS
