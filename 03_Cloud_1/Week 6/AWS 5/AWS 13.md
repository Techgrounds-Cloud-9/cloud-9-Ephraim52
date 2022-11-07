# Files,AppServices,CDN,DNS,Database
Independent assignment to learn about services related to the Database.

## Key terminology
### Elastic Beanstalk= 
A service that deploys, manages and scales web apps and services for you. Using manage containers to support programming language environments on familar servers.(This PaaS is free of charge; only the connected resources have costs.) 

Elastic beanstalk leverages familar AWS services:

- EC2
- S3
- Simple notification service
- Elastic load balancing
- Auto scaling

The benefits of this are:
- It is a more simplified and fast way to upload & deploy your web applications.
- You can directly focus on writing the code instead of the provisioning of having to manage infrastructure.
- Select and retain full control of the optimal AWS resources for powering your applications.
- Use adjustable settings to scale your application for handling peaks in traffic, while minimizing costs.

### CloudFront= 
A Content Delivery Network Service that works with both AWS services as well as your own Origin, its high performance, secure, and made for user/developer convenience its easier to work with than doing everything manually as it helps to manage the deployment & traffic tasks.

Some AWS services that are connected/required for CloudFront:
- You can use AWS services EC2 and S3 or use your own origin server.
- Use AWS certification manager to get a TLS certificate or import your own certificate to encrypt your communications/traffic.
- With Lamba app edge you can run complex application lodges closer to your customers, scale and replicate your application globally without your own origin and go serverless.

Benefits are:
- Fast and global, reducing the latency by delivering data through Points of Presence (PoP) with automated network mapping and intelligent routing. (Using edge locations (PoPs) to deliver static and dynamic content.)
- Highly secure, Amazon traffic encryption, access controls and the use of their AWS Shield standard to defend against DDoS attacks without any charge or cost.
- Programmable, Customize the code you run at the AWS content delivery network (CDN) edge using serverless compute features to balance cost, performance, and security.
- Compliance, Complient with a wide range of standards to ensure delivery of the most sensitive data.
- Cost effective, Cut costs with consolidated requests, customizable pricing options, and zero fees for data transfer out from AWS origins. (Pay as you go)

### Route 53= 
A DNS service that gives developers & businesses a cost effective way to route end users to internet applications. This service has 100% availability, integrates with other AWS services, helps arrange/manage your traffic flow which provides an easy failover to route end users to another location if the final end point becomes unavailable.

Services that can be connected to Route 53 are:
- Load balancers
- EC2 instances
- S3 Buckets
- CloudFront distributions

Benefits are:
- Route end users to your site reliably with globally-dispersed Domain Name System (DNS) servers and automatic scaling.
- Set up your DNS routing in minutes with domain name registration and straightforward visual traffic flow tools.
- Customize your DNS routing policies to reduce latency, improve application availability, and maintain compliance.

### RDS= 
A service that simplifies database management by automating time consuming administration tasks. By automating this management process you have time available to focus on optimization and getting faster results. Wide choice of types of databases to use which are build for the Cloud in AWS. 

Database engines that can be used with RDS are:
- Amazon Aurora with MySQL
- Amazon Aurora with PostgreSQL
- MySQL
- MariaDB
- PostgreSQL
- Oracle
- SQL server
And deploy on premises with Amazon RDS on AWS Outposts.

Benefits are:
- The removal of time-consuming database administration tasks without needing to provision infrastructure or maintain software.
- Deploy and scale the RDS engines of your choice in the cloud or on premises.
- Achieve high availability with Amazon RDS multi-AZ deployments. (failover database protection)
- Benefit from over a decade of proven operational expertise, security best practices, and innovation in databases born in the cloud.

### EFS= 
Elastic File System is a simple and fully managed cloud native system. It simplifies the storage capabilites of the connected services as it automatically scales up and down to what is needed in terms of files being added or removed. You can see this in the EFS storage tab when you work with an EC2 instance where you add files and later on remove them or some of them.

Services that are connected to EFS:
- EC2 instances

Benefits of EFS are:
- Creating a shared file system simplifies and speeds up AWS compute services. (No provisioning, deploying, patching, or maintaince required.)
- Your file system scales automatically as its shared. As files are added or removed to scale the amount of storage up or down automatically accordingly with the changes made to the files.
- This way you only pay for the storage you use, as mentioned earlier the storage scales with EFS as its shared and automatically changes when a file is being worked on. Automatically moves infrequently accessed files and can reduce costs up to 92%.
- Securely and reliably access your files with a fully managed file system designed for 99.999999999 percent (11 9s) durability and up to 99.99 percent (4 9s) of availability.

### Cloud native= 
Cloud-native architecture and technologies are an approach to designing, constructing, and operating workloads that are built in the cloud. (and take full advantage of the cloud computing model.)

### Aurora= 
A fully managed database service that is compatible with MySQL and PostgrSQL. Scales up and down the database to match application demands saving time, and costs.

Services that Aurora can be connected with:
- Amazon AWS RDS
- Amazon S3
- AWS backup
- Amazon DevOps Guru
- AWS CloudTrail
- Amazon Redshift
- Amazon CloudWatch
- Amazon SageMaker
- Amazon Comprehend
- AWS Lambda
- Amazon EKS

Benefits of Aurora are:
- Power performance-intensive applications and critical workloads while maintaining full compatibility with MySQL and PostgreSQL at one-tenth the cost of commercial databases.
- Build applications with Multi-AZ availability backed by a 99.99% uptime SLA and global replication with cross-Region disaster recovery in less than 1 minute.
- Improve productivity and lower total cost of ownership with a fully managed database including innovations like serverless so you can focus on building applications that delight your users.
- Easily migrate MySQL or PostgreSQL databases to and from Aurora using standard tools, or run legacy SQL Server applications with Babelfish for Aurora PostgreSQL with minimal code change. 

## Exercise
EFS, RDS and Aurora how to add these to the previous practical exercises (AWS 10 and 11) to make a fully functional database server with automated processess.

- Create two EC2 instance
- Add keys to both instances
- Create an EFS
- Attach the EFS to the EC2 instance created earlier
- Attach the EFS to the second EC2 instance 

- Create the RDS with the following requirements:
    - For engine type select Aurora
    - Settings name the Database cluster identifier
    - Credentials settings only provide a password to secure access
    - Instance configuration change to burstable classes
        - select db.t3.small as your database setting
    - Connectivity select connect to an EC2 compute resource
    - Use the default VPC
    - Public access select: Yes, you want to access your resources from the outside.

- Create a file in the first EC2 instance
- Check if the file is present in the second EC2 instance, is it writable? No?
- Give write permission to the file in the first instance, for this exercise we just decided to check if the file was available for the other instance as well.
- Check in the second instance if you have write permission to demonstrate the shared file system.

- After creation check the RDS Databases tab and go to connectivity & security
- Check monitoring as well, now you should see the changes made in the graphs from when you worked with the file for the EC2 instance.

### Sources
https://aws.amazon.com/elasticbeanstalk/

https://www.youtube.com/watch?v=SrwxAScdyT0

https://aws.amazon.com/cloudfront/

https://www.youtube.com/watch?v=AT-nHW3_SVI

https://aws.amazon.com/route53/?nc2=type_a

https://www.youtube.com/watch?v=RGWgfhZByAI

https://aws.amazon.com/rds/?nc2=type_a

https://www.youtube.com/watch?v=ULRnn6tIYu8

https://www.techtarget.com/searchaws/definition/Amazon-Relational-Database-Service-RDS#:~:text=Amazon%20Relational%20Database%20Service%20(RDS,%2C%20backup%2C%20recovery%20and%20patching.

https://medium.com/awesome-cloud/aws-amazon-rds-vs-amazon-ec2-relational-databases-comparison-b28eb0802355

https://www.youtube.com/watch?v=tLp8pPNdDXQ

https://www.youtube.com/watch?v=eMzCI7S1P9M

https://aws.amazon.com/efs/?nc2=type_a

https://www.youtube.com/watch?v=Aux37Nwe5nc

https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/definition

https://aws.amazon.com/rds/aurora/?nc2=type_a

https://www.youtube.com/watch?v=FzxqIdIZ9wc

https://www.youtube.com/watch?v=vXZLUL309ek

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html

### Overcome challenges
Creating a step by step plan for the execution of a demonstration for the pratical part of the assignment. The main issue seems to me where to apply the RDS to.

### Results
I found the EC2 tab in Services, select Compute menu, select EC2 and create the two instances that you see here.

![alt text]()

Going to Services you see the menu of all services offered, select Storage and select EFS. Now I created an EFS which I attached to both EC2 instances.

![alt text]()

These are the two instances that EFS is attached to.

![alt text]()

Open the services menu again, select the Database menu, and select the RDS service. Now I made the RDS according to the requirements.

![alt text]()

Creating the text file in the VM of the EC2 instance and showing that it is available on the second instance as well.

![alt text]()

Giving permission to file so that the second instance can write in the file as well.

![alt text]()

After this part view in RDS databases the changes from the file in the monitoring tab.

![alt text]()
