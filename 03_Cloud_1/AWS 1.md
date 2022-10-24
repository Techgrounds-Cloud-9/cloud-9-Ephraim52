# AWS Global Infrastructure
Studying the AWS global infrastructure.

## Key terminology
AWS= Amazon Web Services is a cloud computing platform provided by Amazon. 

Regions= Dispersed locations geographically throughout the world.

AWS Availability zones= Availability zones are seperate zones within a region that are available and isolated from the failures in other zones.

Edge locations= These are the locations with data centers that give quick access to speed up connectivity responses.

RDS instance= Relational Database Service is a database instance in the cloud that manages this database instance.

IAM= Identity and Access Management this manages the identities and access priveliges that an identity/user has.

Complaince= If your workload contains data that is bound by local regulations, then selecting the Region that complies with the regulation overrides other evaluation factors. This applies to workloads that are bound by data residency laws where choosing an AWS Region located in that country is mandatory.

Latency/Performance= A major factor to consider for user experience is latency. Reduced network latency can make substantial impact on enhancing the user experience. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. It can also increase communication quality, given that network packets have fewer exchange points to travel through.

Cost= AWS services are priced differently from one Region to another. Some Regions have lower cost than others, which can result in a cost reduction for the same deployment.

Services & Features= Newer services and features are deployed to Regions gradually. Although all AWS Regions have the same service level agreement (SLA), some larger Regions are usually first to offer newer services, features, and software releases. Smaller Regions may not get these services or features in time for you to use them to support your workload.

## Exercise
- What is an AWS Availability Zone?
- What is a Region?
- What is an Edge Location?
- Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).

### Sources
https://www.techtarget.com/searchaws/definition/Amazon-Web-Services

https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/RegionsAndAZs.html

https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/#:~:text=Edge%20locations%20are%20AWS%20data,can%20be%20fast%20and%20snappy.

https://docs.rightscale.com/cm/dashboard/clouds/aws/rds_instances.html

https://www.noraonline.nl/wiki/Identity_%26_Access_Management_(IAM)

https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/

### Overcome challenges
Just looking for the information, lots of reading.

### Results
Why would you choose one region over another?

- The impact on complaince
- Costs
- Performance
- Services available to work with

These are factors to keep in mind with choosing a region as they impact the limit to which you can work optimally within the AWS cloud. I would choose the Frankfurt region as it is based on the European continent and has a better complaince, costs, performance and services to work with. European law, performance because its closer to home, this also impact the costs and services depend on for who you are making any of this.