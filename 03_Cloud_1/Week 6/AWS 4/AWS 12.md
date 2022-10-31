# Well Architected Framework
What does WAF look like and what do the pillars mean.

## Key terminology
KPIs= Key performance indicators based on data from measurements of performance over time of a specific service/application for a specific objective. Like looking what can be improved about a certain service/application.

Device farm= A test environment for testing service or other related resources for or with experimental improvements for example. You can also get an overview of the test results.

See you the results for further explanation.

## Exercise
- The Well Architected Framework

### Sources
https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc

https://www.youtube.com/watch?v=x6DIk0_2Goo&list=PLzde74P_a04cyCsmZakYbUE5sWN9dZ-Ux&index=13

https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/the-shared-responsibility-model.html

https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/design-principles-for-sustainability-in-the-cloud.html

https://www.qlik.com/us/kpi

https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-use-reports.html

### Overcome challenges
Learning through reading.

### Results
Well Architectured Framework
-	Helps you understand the pros and cons of decisions you make while building systems on AWS.
-	Based on 6 pillars:
-	Operational Excellence pillar
    -	Support development and run workloads effectively.
    -	Gain insight into workload operations.
    -	Continuously improve processes and procedures to deliver business value.
-	Best practices for Operational Excellence:
    -	Perform operations as code not manually use tools like cloudformation to automatically build your infrastructure.
    -	Make frequent, small, reversible changes as this helps you when something goes wrong you can quickly roll back and try again.
    -	Refine operations procedures frequently, constantly re-evalute to look if there’s a better way to do or improve things.
    -	Anticipate failure to help prevent failures from happening and also to recover from any potential failures.
    -	Learn from all operational failures make sure you update your procesess, work out why did it happen and what can I do next time.

-   Security pillar
    -	Protect data, systems, and assets to take advantage of cloud technologies to improve your security.
-	Best practices for Security:
    -	Implement a strong identity foundation, like IAM identity systems to secure identities and give the right accessess to these identities.
    -	Enable traceability, trace what is happening and to see where things go wrong.
    -	Apply security at all layers, make sure to secure all layers not just the foundation for total security of your data/application.
    -	Automate security best practices, the more you automate the less human error you are bound to have and to make it easier.
    -	Protect data in transit and at rest, like encrypting your data.
    -	Keep people away from data, have the right access controls in place to secure your data access.
    -	Prepare for security events, prepare in case anything happens like malicious attacks.

-	Reliability pillar
    -	Ensuring a workload can perform its intended function correctly and consistently when it’s expected to.
    -	This includes the ability to operate and test the workload through its total lifecycle.
- Best practices for Reliability:
    -	Automatically recover from failure, make sure you automatically recover from failures so you don’t have to manually be involved. (EC2 auto-scaling)
    -	Test recovery procedures, to make sure they work so that they function when a failure occurs.
    -	Scale horizontally to increase aggregate workload availability, to ensure a single failing component does not affect the entire system or application. (dynamoDB and EC2 instances)
    -	Stop guessing capacity, dynamically and automatically change the amount of resources we assign/associate to our application.
    -	Manage change in automation, implement change management procedures and automate as much as possible.

-	Performance Efficiency pillar
    -	The ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve.
-	Best practices for Performance Efficiency:
    -	Democratize advanced technologies, to use AWS their services to increase the value of your business through efficiency.
    -	Go global in minutes, by deploying your applications anywhere in the world at any time.
    -	Use serverless architectures, not having to manage the underlying infrastructure and this gives the ability to scale more and use a higher level of services.
    -	Experiment more often, it is easy to do in the cloud and you can learn a lot of different things regarding services about what we do and how to improve those services as well as performances.
    -	Consider mechanical sympathy, understand the systems and purpose of those systems that are available to you to utilize them to their best effect.

-	Cost Optimization pillar
    -	The ability to run systems to deliver business value at the lowest price point.
-	Best practices for Cost Optimization:
    -	Implement Cloud Financial Management 
    -	Adopt a consumption model, for what you use in AWS.
    -	Meassure overall efficiency, constantly meassure if you are using your systems optimally, to see if you are using the right pricing models and if you have not overallocated resources.
    -	Stop spending money on undifferentiated heavy lifting, not building your physical datacenter and infrastructure instead use AWS cloud services and infrastructure which is already in place to build you product.
    -	Analyze and attribute expenditure, which items cost what and where exactly the costs are coming from.

-	Sustainability pillar
    -	Is a process of continuously looking for better ways to sustain your shared infrastructure, resources (like water, power and hardware) and delivering in an efficient way.
    -	Optimize workloads, resource utilization, and minimizing the total resources required to be deployed for workloads.
-	Best practices for Sustainability:
    -	Region selection, choosing regions that use renewable energy and have lower carbon intensity than other locations.
    -	User behaviour patterns, scale infrastructure to match workload and use only the minimum amount of resources, identify improvements, created and unused assets to reduce impact.
    -	Software and architecture patterns, improve the utilization of deployed resources to minimize consumption, implement patterns to increase overall utilization of under-utilized components and retire components that are no longer required.
    -	Data patterns, use data management to reduce the storage required for your workload and resources required to use it in order to increase efficiency and support the business value. (lifecycle data to more efficient  or when requirements decrease delete data)
    -	Hardware patterns, reduce workload sustainability impacts to hardware management, minimize the amount of hardware needed to provision and deploy, select the most efficient hardware for your (individual) workload.
    -	Development and deployment process, improve sustainability by making changes to your development, test potential improvements, keep everything up-to-date, use automation to maximize utilization of development and test environments, use test farms for testing the impact of changes.
