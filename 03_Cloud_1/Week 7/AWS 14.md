# Cloud Fundamentals
Study the terms and see how they work in practice.

## Key terminology
### ECS= Elastic Container Service 
providing higly scalable and high performance container management service, allows you to easily run applications on a managed cluster of EC2 instances.

Services involved with ECS
- Amazon EC2
    - You explicitly provision EC2 instances
    - You’re responsible for upgrading, patching, care of EC2 pool
    - You must handle cluster optimization
    - More granular control over infrastructure (fine-grained)
- Amazon Fargate
    - The control plane asks for resources and Fargate automatically provisions
    - Fargate provisions compute as needed
    - Fargate handles cluster optimization
    - Limited control, as infrastructure is automated
- ECR= Elastic Container Registry is a managed AWS Docker registry service for storing, managing, and deploying Docker images.

Benefits of ECS are:
- Fully automated service with no control plane to manage, use automation tools
- With ECS Anywhere people can work with containers anywhere on a cloud or on premises environments.
- Combining ECS with Fargate you don't have to manage hosts, no patching, upgrading or maintaining.
- ECS delivers Security control from end to end
- Overall giving you more time to spend on your projects, rather then managing the resources around it.
- Save up to 50 percent on compute costs with autonomous provisioning, auto-scaling, and pay-as-you-go pricing.

### AWS Support Plans=
A choice of Plans from AWS to offer Support to your organization based on your needs. providing you with the right mix of tools and expertise so that you can optimize performance, manage risk, and limit costs.

For more details look at the AWS support plans webpage for their specific package with plans to help grow your business or in my case for my exam.

### Trusted Advisor= 
Available to AWS Enterprise Customers from the AWS Support Plans. Giving you an overview from the AWS account team and machine generated checks to improve your business and the services/resources you use.

Connected resources to Trusted Advisor are:
- RDS DB
- EBS
- Lambda
- EC2
- CloudFront
- S3 buckets
- Security groups
- Auto-scaling
- Route 53

Benefits from Trusted Advisor are:
- Cost Optimization saving you costs with recommendations you can act upon improving your business and to make it more efficient improving the business value by reducing the costs of unneeded processes.
- Perfomance with actionable recommendations from analytic data you can improve your business efficiency. 
- Security giving you best practice security recommendations to reduce security risk like having a snapshot with public access and warning you that this access option is a security risk for you asking you to reduce it by taking action and changing access permissions to the snapshot.
- Fault Tolerance providing you with advice that can help improve reliability like auto-scaling or automating processes to reduce human error.
- Service Quotas is the maximum amount of resources you can create in an AWS account. AWS implements quotas to provide highly available and reliable service to all customers, giving you advice to reduce or delete resources that provide unintentional spendings.

### AWS Config=
A service where you can assess, audit, and evaluate configurations for all your AWS resources. Define policies and configurations and receive warnings if there is a deviation from these rules, provides automatic remediation. Helps you check if your resources configurations comply with government regulations and best practices accross all regions.

AWS Config service works with:
- EC2
- AWS config API's and console
- Amazon SNS
- Amazon CloudWatch
- Amazon S3

Benefits of AWS Config service are:
- Continually assess, monitor, and record resource configuration changes to simplify change management.
- Audit and evaluate compliance of your resource configurations with your organization’s policies on a continual basis.
- Simplify operational troubleshooting by correlating configuration changes to particular events in your account.

### AWS Cloud Trail= 
A service that monitors changes and detects them to give you an overview of the activity on your resources when and where. Works accross all regions and integrates with other AWS services. Providing security automation to act fast to fix these problems and giving less worries.

Services that Cloud Trail uses or monitors:
- Amazon S3
- Cloudwatch
- Cloud Trail Insights
- Amazon EventBridge
- Amazon Athena

Benefits of Cloud Trail:
- Protects your organisation by showing that you comply with regulations (compliance).
- Security is improved by recording User activity and setting up automated workflow rules.
- Capture and consolidate user activity and API usage across AWS Regions and accounts on a single, centrally controlled platform.

### IAM= Identity & Access Management
Allows you to determine which user/account has access to which resources or services, you can also centralize it by making groups that contain users that have permission to access specific resources and services.

Works with the following services/resources:
- Cloud Trail
- EC2
- Generally to manage access permissions for all services and resources.

Benefits of IAM are:
- Use fine-grained access controls to control who has access to what.
- Manage identities single accounts or multiple accounts as groups to centrally manage them.
- The ability to temporarely give access to anyone for using your resources.
- Continually analyze access to right-size permissions on the journey to least privilege.

### AWS CloudWatch=
CloudWatch monitors the resources and applications you run on AWS in the cloud.

Monitors the following resources:
- EC2 instances.
- DynamoDB tables.
- RDS DB instances.
- Custom metrics generated by applications and services.
- Any log files generated by your applications.

Benefits of CloudWatch are:
- Collect, access, and analyze your AWS data using powerful visualization tools.
- Operational performance can be improved by using alarms and automated actions set to activate when the limit or set rule is reached/breached.
- Seamlessly integrate with more than 70 AWS services for simplified monitoring and scalability.
- Troubleshoot operational problems with actionable insights derived from logs and metrics in your CloudWatch dashboards.

### DynamoDB=
Is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.

Services that DynamoDB uses:
- Amazon S3
- AWS Glue Elastic Views
- Amazon Kinesis Data Streams
- AWS Cloud Trail
- Amazon CloudWatch

Benefits of DynamoDB are:
- Fast and high performance, automatic multi-Region replication.
- Secure data with encryption at rest, automatic backup and restore, and guaranteed reliability of up to 99.999% availability.
- Focus on innovation and optimize costs with a fully managed serverless database that automatically scales up and down to fit your needs.
- Integrate with AWS services to do more with your data. Use built-in tools to perform analytics, extract insights, and monitor traffic trends.

### AWS Lambda=
AWS Lambda is a serverless computing technology that allows you to run code without provisioning or managing servers. AWS Lambda executes code only when needed and scales automatically. You pay only for the compute time you consume (you pay nothing when your code is not running). (SaaS)

Works with different programming languages and platforms.
- .NET
- .NET Core
- Go
- Java
- Node.js
- Python
- Ruby

Services/resources that AWS Lambda uses:
- Amazon S3
- AWS EFS
- Amazon Kinesis
- Amazon DynamoDB
- Amazon API Gateway
- Amazon SNS

Benefits of AWS Lambda are:
- No servers to manage.
- Continuous scaling.
- Millisecond billing.
- Integrates with almost all other AWS services.

###  AWS SNS= 
Simple Notification Service makes it easier to manage and send notifications from the cloud to for example users of your application.

Usage of SNS:
- Send automated or manual notifications.
- Send notification to email, mobile (SMS), SQS, and HTTP endpoints.
- Closely integrated with other AWS services such as CloudWatch so that alarms, events, and actions in your AWS account can trigger notifications.

Benefits of AWS SNS are:
- Reliable 
- Scalable
- Simple
- Flexible 
- Secure
- Inexpensive

For explanation about about the benefits check the links in sources.

### AWS SQS= 
Amazon Simple Queue Service (SQS) is a distributed queue system. Amazon SQS enables you to send, store, and receive messages between software components. An Amazon SQS queue is a temporary repository for messages that are awaiting processing. The SQS queue acts as a buffer between the component producing and saving data, and the component receiving the data for processing.

Services SQS uses:
- EC2 instances
- Auto-scaling group

Benefits of SQS are:
Same as SNS.

### Event Bridge=
Used to be named CloudWatch Events observes events and direct them if programmed to. Being a serverless event bus that receives, filters, transforms, route, and deliver events to connected service/resources. So they work more independently, so less work for you and more time to spend on other parts of your work.

Works with any serice and resource.

Benefits of EventBridge are:
- Easy to build and helps deploy new features faster.
- Ingest, filter, transform, and deliver events from connected applications—without writing custom code or managing and provisioning servers.
- Connect AWS services, software-as-a-service (SaaS) applications, and custom applications as event producers to launch a variety of workflows.
- Automatically scale based on the number of events ingested, and pay only for events published by your AWS or SaaS applications.

### SLA=
Service Level Agreement The requirements the services of AWS need to meet which are standard for delivering a good functioning and reliable service.

### NoSQL=
NoSQL is a database in which you can store files that are only documents, graphs, key-value, and wide-column. NoSQL is not a relational table in comparison to MySQL which is a relational table. Scale horizontally, easier to manage, performs better through simplicity, more functional.

## Exercise
- Describe where you can find the following services
- How you can use these services
- Is it possible to connect these services with other services/resources?

These are the services for this exercise:
- IAM
- AWS CloudWatch
- DynamoDB
- AWS Lambda
- SNS, SQS, Event Bridge

- Set up an EC2 instance
- Connect this with the default VPC
- Setup CloudWatch
- Create an connect the following services:
    - SNS
    - SQS
    - Event Bridge
    - Add Lambda to SNS, to program an action or alarm.
- Create a DynamoDB
- Attach the DynamoDB to the EC2 instance
- Test the rule or alarm you set with SNS Lambda.
- Check for any changes in CloudWatch and the other services.

### Sources
https://www.youtube.com/watch?v=FnFvpIsBrog

https://aws.amazon.com/ecs/

https://digitalcloud.training/aws-compute-services/

https://us-east-1.console.aws.amazon.com/support/plans/home?region=us-east-1&skipRegion=true#/

https://www.youtube.com/watch?v=Jb1gb1g9Nw0

https://aws.amazon.com/premiumsupport/technology/trusted-advisor/

https://www.youtube.com/watch?v=MJDuAvNEv64

https://aws.amazon.com/config/?nc2=type_a

https://aws.amazon.com/cloudtrail/?nc2=type_a

https://www.youtube.com/watch?v=mXQSnbc9jMs

https://www.youtube.com/watch?v=Ul6FW4UANGc

https://aws.amazon.com/iam/?nc2=type_a

https://www.youtube.com/watch?v=a4dhoTQCyRA

https://aws.amazon.com/cloudwatch/?nc2=type_a

https://www.youtube.com/watch?v=eOBq__h4OJ4

https://aws.amazon.com/lambda/?nc2=type_a

https://aws.amazon.com/dynamodb/?nc2=type_a

https://www.youtube.com/watch?v=sI-zciHAh-4

https://aws.amazon.com/sns/details/

https://www.youtube.com/watch?v=8BEwZnUIZfw

https://docs.aws.amazon.com/sns/latest/dg/welcome.html

https://digitalcloud.training/aws-application-integration/#amazon-simple-queue-service-amazon-sqs

https://www.couchbase.com/resources/why-nosql#:~:text=NoSQL%20databases%20store%20data%20in,column%20databases%2C%20and%20graph%20databases.

https://www.youtube.com/watch?v=MBODF1Vru2Y

https://aws.amazon.com/legal/service-level-agreements/?aws-sla-cards.sort-by=item.additionalFields.serviceNameLower&aws-sla-cards.sort-order=asc&awsf.tech-category-filter=*all

https://aws.amazon.com/eventbridge/

https://aws.amazon.com/nosql/

### Overcome challenges
Reading and looking at some extra sources for certain services to have a clearer view. 

### Results
This is a list to summarize where you can find the services mentioned in the Exercise part:
- For IAM go to Services, click on Security, identity & compliance, and click on IAM
- For AWS CloudWatch go to Services, click on Management & Governance, and click on CloudWatch.
- For DynamoDB go to Services, click on Database, and click on DynamoDB.
- For AWS Lambda go to Services, click on Compute, and click on Lambda.
- For SNS, SQS, EventBridge go to Services, click on Application Integration, and click on either SNS, SQS or EventBridge all three of these services can be found in this menu.

I created a Test user with the IAM service, setting different permissions for different services/resources.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_IAM_user_created.png)

Made the DynamoDB with default settings just for checking what I can connect it with.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_DynamoDB_with_CloudWatch.png)

Made an alarm notification with a SNS topic, to receive alerts when the capacity that is provisioned for the DynamoDB is greater than 8000.

CloudWatch

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_SNS_created_in_CloudWatch.png)

SNS Topic

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_SNS_Topic.png)

Connecting SNS Topic with CloudWatch.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_CloudWatch_connected_SNS.png)

When I made the SQS I needed to make a function was well with Lambda which you can see in these screenshots.

SQS

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_SQS_created.png)

Lambda function

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_Lambda_function.png)

Lamba function connected with SQS.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_Lambda_with_SQS.png)

As last the EventBridge.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/0b2b2e88fb940cc32011627dec3cce1cc261d47a/00_includes/week%207/AWS14_EventBridge.png)
