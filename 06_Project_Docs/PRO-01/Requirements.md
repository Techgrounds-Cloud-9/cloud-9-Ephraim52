## Demands of the application by the productowner v1.0

- All VM's have to be encrypted
- The webserver has to have a daily created backup, this backup has to be stored for 7 days.
- The webserver has to be installed by an automated process
- The admin/management has to be available through the public IP
- The admin/management server should only be accessible from reliable trustworthy locations
- These IP ranges are available for usage 10.10.10.0/24 & 10.20.20.0/24
- All subnets have to be protected by a firewall on the subnet level
- SSH or RDP connections with the webserver are only allowed from the admin server
- Improve the architecture where needed and keep it real in order to meet the deadline

## Assumed demands of the application for the architecture v1.0

Infrastructure
- VPC - Region
- Public subnet - Availability Zone, the IP ranges are set for the subnet
- Internet Gateway - Attached to the Public Subnet for connection with the internet
- VPC peering to connect both the servers to eachother, connection rules defined by ACL and SG
- ACL's as firewall on subnet level
- Security groups as firewall on the instance level
- Create Backup vault plans to ensure that Backups are created on a daily basis and that these are saved for 7 days
- Two instances in 2 different availability zones to set up the admin server and webserver individually
- AMI is needed to setup the EC2 instance as a launch template
- Add KMS - for encrypting and decrypting the data
- EC2 instances attached to the VPC to ensure it runs and has the right access
- S3 storage for Bootstrap scripts to give it userdata when the instance is deployed. This will give shape to the 
instance when being looked at by the public

IAM
- assign roles to services
- least privilege
- rotate keys regularely - KMS optional
- Use the SSH keys for access to webserver

## Resources required for v1.0
- VPC
- EC2
- S3
- Security Groups
- Network access control lists
- IAM roles
- Backup vault
- KMS

## Demands of the product owner for v1.1

- De webserver moet niet meer “naakt” op het internet te benaderen zijn. Het liefst ziet de klant dat er een proxy 
tussen komt. Ook zal de server geen publiek IP adres meer moeten hebben.
- Mocht een gebruiker via HTTP verbinding maken met de load balancer dan zou deze verbinding automatisch geupgrade 
moeten worden naar HTTPS.
- Hierbij moet de verbinding beveiligd zijn met minimaal TLS 1.2 of hoger.
- De webserver moet met enige regelmaat een ‘health check’ ondergaan.
- Mocht de webserver deze health check falen dan zou de server automatisch hersteld moeten worden.
- Mocht de webserver onder aanhoudende belasting komen te staan dan zou er een tijdelijke extra server opgestart 
moeten worden. De klant denkt dat er nooit meer dan 3 servers totaal nodig zijn gezien de gebruikersaantallen in het verleden.

## Assumed demands for v1.1

- To act as a proxy for the webserver we have to add a load balancer and make sure the IP is no longer public.
- Make sure HTTP upgrades to HTTPS, need a certificate for this to make it work with the load balancer.
- Connection has to be secured with at least TLS 1.2 or higher.
- The health check is connected to the load balancer so that with the faulty check customers get re-routed to
the next instance with the Webserver.
- On a failed health check the failed instance needs to be automatically restored with the last working backup file from the vault.
- If the webserver is being overloaded there has to be an extra webserver available though not more then 3 server which we will
use autoscaling group for. This will allow scaling to demand and scale down if demand is low.
- Backupvault is no longer required as the webserver has no data on it aside of the userdata and ami. Which both in
their own way can be provided as a backup.

## Resources required for v1.1
- Certificate Self signed not acquired through AWS
- Load Balancer
- Health checker is part of the LB
- Autoscaling group
- (IAM roles) according to least privilege
- HTTPS connection needs to be adjusted to the new demands.
