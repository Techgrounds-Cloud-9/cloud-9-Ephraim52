# Shared Responsibility Model
Understanding the Shared Responsibility Model concept.

## Key terminology
See results for explaination about the shared responsbility model.

## Exercise
- The AWS Shared Responsibility Model

### Sources
https://www.youtube.com/watch?v=iODPCcQEPto&list=PLzde74P_a04cyCsmZakYbUE5sWN9dZ-Ux&index=38

https://aws.amazon.com/compliance/shared-responsibility-model/

### Overcome challenges
Just learning through reading.

### Results
Shared Responsibility Model
Customer – responsibility for security ‘in’ the cloud.

- 	Customer data – completely responsible for your own data – you decide what data goes where and is stored through which service and rules
- 	Platform, applications, identity & access management - which users have access to which platforms or services/applications
- 	Operating system, network & firewall configuration – responsible for managing the OS yourself as well as the settings you configure for the network and firewall
- 	Client-side data, encryption & data integrity, authentication
- 	Server-side encryption (file system and/or data)
- 	Networking traffic protection (encryption, integrity, identity) – as customer you are responsible for choosing who has access and how to encrypt your data, where the data has to be routed to

AWS – responsibility for security ‘of’ the cloud
- 	Software
- 	Compute, storage, database, networking (hardware) – responsible for maintaining the hardware (no errors occur)
- 	Hardware/AWS Global infrastructure
- 	Regions, Availability Zones, Edge Locations

Concept points:
- 	The AWS shared responsiblity model defines what you (as an AWS account holder/user) and AWS are responsible for when it comes to security and compliance.
- 	This is in relation to Security & Compliance which is a shared responsibility between AWS and the customer.
- 	AWS are responsible for “Security of the Cloud”.
    - 	AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS cloud.
    - 	This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud Services.
- 	Customers are responsible for “Security in the Cloud”.
    - 	For EC2 this includes network level security (NACLs, security groups), operating system patches and updates, IAM user access management, and client and server-side data encryption.

- 	Inherited Controls – Controls which a customer fully inherits from AWS.
    -	Physical and Environmental controls
-	Shared Controls – Controls which apply to both the infrastructure layer and customer layers, but in completely seperate contexts or perspectives.
    -	Path management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
    -	Configuration management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.
    -	Awareness & Training – AWS trains AWS employees, but a customer must train their own employees.

-	Customer Specific – Controls which are solely the responsibility of the customer based on the application they are deploying within AWS services. Examples include:
    -	Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.

With EC2 for example a customer would be responsible for how to deploy their instance and how to provide the data and secure that data with encryption not only for themselfs but for the users that can use the instance as well. The instance needs the customer to manage the ACls to control who has access to which part of the instance.

AWS has the responsbility here to maintain the hardware for this instance and the software has to be kept up-to-date which the customer uses. 

As you can read the customer has a lot more responsibilities and details to be aware of than AWS.