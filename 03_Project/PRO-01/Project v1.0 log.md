# Log

## One Sentence summary of the day

## Challenges

## Solutions

## Learnings

# Log 28-11-2022

## One Sentence summary of the day
Studying the CDK and how it works

## Challenges
Figuring out how CDK works, after not finding a proper explanation. I looked at different services that matched this and in Cloud9 it seems you can create an environment.

## Solutions
Create plans and design infrastructure.

## Learnings
Time management as we are working with a deadline time management is vital to achieving the desired result by the end of the time we have. Setting up steps to create the Code as Infrastructure.

# Log 30-11-2022

## One Sentence summary of the day
Studying the CDK and creating a vpc stack

## Challenges
Figuring out how to connect the VPC stack with the main app.py file, to synthesize it to get a template.

## Solutions
Read and watch a lot look at other constructs or templates.

## Learnings
Learned how to connect the vpc stack with the main app.py file and whether it needed to be seperate stacks or one whole stack of resources. The connection was corrected by specifying the variables of the files in sync with eachother.

# Log 01-12-2022

## One Sentence summary of the day
Re-creating the vpc starting fresh, along with setting up the ACL's for the subnets.

## Challenges
Creating the ACL policies to grant access to specific resources.

## Solutions
Read and watch a lot look at other constructs or templates, to get a better understanding.

## Learnings
A policy is complicated and exists out of various variables that need to be assigned the values that set up the access rule.

# Log 02-12-2022

## One Sentence summary of the day
Re-creating the vpc starting fresh, along with setting up the ACL's for the subnets.

## Challenges
Creating the ACL policies to grant access to specific resources.

## Solutions
Found the solution when going through the AWS API list looking for ACL entries, where it showed a small model of what it should look like.

## Learnings
How to create an ACL and the Entry rules that allow or deny access.

# Log 05-12-2022

## One Sentence summary of the day
Looking into KMS to create keys and use them for encrypting data.

## Challenges
Finding information about KMS on how to put it into code.

## Solutions
Read and watch a lot look at other constructs or templates, to get a better understanding.

## Learnings
That it is possible if you create a client with boto3.

# Log 06-12-2022

## One Sentence summary of the day
Working on making the KMS and the client needed to create the keys.

## Challenges
Creating KMS part and figuring out how to create a client without third parties being required.

## Solutions
Read and watch a lot look at other constructs or templates, to get a better understanding.

## Learnings
Its pretty hard to setup a KMS client as it requires different programming languages as well. 
I am looking into other ways to make this work.

# Log 07-12-2022

## One Sentence summary of the day
Realized I could also encrypt using the .pem file in which our key is stored and the public key that is generated at that moment as well.

## Challenges
How to set this up and how to add the .pem file with KMS in order to make sure its managed and used for encrypting.

## Solutions
Read and watch a lot look at other constructs or templates, to get a better understanding. Even discuss the possibilities.

## Learnings
That it is possible to configure it in this way, just need a better understanding of how to do this.

# Log 08-12-2022

## One sentence Summary of the day
Did encryption in another way without creating KMS and just assigning encryption to the resources that needed it.

## Challenges
At that time I was reading into a way to just encrypt it by each seperate resource that needs it.

## Solutions
Figured out that if you hovered over a parameter you would see the explanation, but also in that note you can scroll down and its where I found some lines that explained how to encrypt for example the S3 Bucket.

## Learnings
Learned how to encrypt S3 bucket in particular and will apply this for the other resources that need it.

# Log 09-12-2022

## One sentence Summary of the day
Figuring out how the userdata can be used for the instance to deploy a website with a visible webpage.

## Challenges
Making the userdata readable for the instance to use.

## Solutions
Trying various ways in writing permission to download, execute and give read permission to the instance.

## Learnings
I learned that I need to dive deeper into this to understand why the instance is not using the userdata.

# Log 12-12-2022

## One sentence Summary of the day
Still wrestling with the userdata and attempted the various way to use it for the instance.

## Challenges
Its not working with the various commands and permissions.

## Solutions
Need to delve deeper into this part still and check my code piece by piece. As to figure out if there is an error in any of the resources.

## Learnings
That the error might not be in the deployment of the userdata but rather in the code itself for example Nacls.

# Log 13-12-2022

## One sentence Summary of the day
Doing a full check on my code to right the wrongs.

## Challenges
Going through the code multiple times and figuring out through deployment of the code where the problem for the userdata is exactly.

## Solutions
Discuss it with my peers to learn from their insights.

## Learnings
Learned that Nacls have ephemeral ports that work in ranges which needs to be specified for certain entries.

# Log 14-12-2022

## One Sentence summary of the day
Fixed the userdata issue and the problem in the Nacls.

## Challenges
Finding the Nacls that create the issue on using the userdata for the Webserver instance.

## Solutions
As mentioned in the previous log setting the ranges for ephemeral ports for some of the Nacls entries.

## Learnings
Problem is not always with the resource you are working on it might also be in an earlier made resource. 

# Log 15-12-2022

## One Sentence summary of the day
Connecting with RDP and SSH to the Webserver

## Challenges
Couldn't connect with RDP to the Admin Server or even use SSH to connect further to the Webserver.

## Solutions
Change the IP and ports to make the connections.

## Learnings
Creating a Nacl is hard work there is always something in the rules that isn't properly connected like 
the ports or having to specify an IP address.

# Log 16-12-2022

## One Sentence summary of the day
Creating a backup vault and connecting this to the existing backup plan, so that it is removed on cdk destroy.

## Challenges
I first tried on a couple of other ways to allow it to be destroyed when using cdk destroy. Like creating a seperate 
rule for RemovalPolicy and link that to the backup plan.
## Solutions
though because it didn't work I still ended up making a seperate vault with the RemovalPolicy included.

## Learnings
Just try the work you find annoying from the start rather than trying to go around it as that didn't work.

# Log 19-12-2022

## One Sentence summary of the day
Starting the week on v1.1 making the epics.

## Challenges
Adjusting the diagram to the current requirements of v1.1

## Solutions
Over time I will gain more insight into what is specifically required for v1.1 as well as maybe something can be added from best practice to even improve this version.

## Learnings
Learning takes time. A lot...

# Log 20-12-2022

## One Sentence summary of the day
Working on the RDP and SSH connection from the Admin server to the Webserver.

## Challenges
It won't create the SSH connection from the Admin server to the Webserver. Have to check if this is a problem coming from the NACLs or the SG's.

## Solutions
Haven't found it yet but the RDP connection is working. I am however convinced it is something in the NACLs.

## Learnings
Need to read up more on SSH connection about being established through NACLs in code.

# Log 21-12-2022

## One Sentence summary of the day
Adjusted my cidr block from 26 to 25 and set the vpc and subnets to span 2 availability zones.

## Challenges
It kept giving the error that "A construct with that name 'VPC-Web peer route' already exists." even when I changed this string which seemed to be mentioned on a lot of website as the issue it kept giving the error.

## Solutions
The problem was in the for loop of the peering connection as it generate a unique string each time it had to run and because of 2 availability zones it had to duplicate this twice which it couldn't do hence the problem as mentioned at challenges. So I removed the for loop and changed the values to connect again to establish the vpc peering once more.

## Learnings
A for loop can also create the same issue with the identifier string as simply having a string with the same value double. For loop in this case spans all AZs you attach it too and as such will always give this error, so I shouldn't have used the for loop to begin with.

# Log 22-12-2022

## One Sentence summary of the day
Applying the Auto Scaling Group to the code and it needs some tweaking.

## Challenges
Finding out how it needs to be connected to the userdata and launch multiple instances up to 3 if the first one is overloaded. How to set a thresshold to make the ASG create the extra instances.

## Solutions
Still looking how to apply the userdata, as for the ASG I set a thresshold at 80% CPU usage if it goes over that then a new instance will be created.

## Learnings
How to set thressholds in code and that userdata is a very hard thing to link to your resources for usage.

# Log 23-12-2022

## One Sentence summary of the day
Managed to create error after error, like an endless cycle.

## Challenges
Fixing the errors one by one.

## Solutions
Starting from scratch again with the experience gained from working on this project.

## Learnings
Seperate stacks are better to troubleshoot then having one stack which becomes hard to read due to it being cluttered.

# Log 09-01-2023

## One Sentence summary of the day
Troubleshooting the Runtime error in my new project environment.

## Challenges
Reading a lot about Runtime and solutions, where to look at.

## Solutions
Tried changing variable names and parameters, didn't work so I keep looking.

## Learnings
Understanding what a Runtime error is.

# Log 10-01-2023

## One Sentence summary of the day
Fixing the Runetime errors by discussing the issue.

## Challenges
Fixing the Runtime error after the discussion.

## Solutions
Work within the rules of the AWS CDK Toolkit as the toolkit has its own rules python rules don't always apply.
Simply said you are working in a Framework.

## Learnings

# Log 11-01-2023

## One Sentence summary of the day

## Challenges

## Solutions

## Learnings

# Log 12-01-2023

## One Sentence summary of the day

## Challenges

## Solutions

## Learnings

# Log 13-01-2023

## One Sentence summary of the day

## Challenges

## Solutions

## Learnings

# Log 16-01-2023 

## One Sentence summary of the day
Sending out job interviews and writing the nacls for the private subnet of the webserver.

## Challenges
Writing motivation letters over and over specific to the companies I applied for.

## Solutions
Have like a standard template written by myself ready, editing only some minor adjustments to
specify it towards the company I apply to.

## Learnings
Never forgot to edit or change the motivation letter.

# Log 17-01-2023

## One Sentence summary of the day
Job interviews no time for the project sadly.

## Challenges
At first everything during the interview seemed positive, though what they actually want is more specific
technical questions that show a certain interest in them as a company on what they provide for their
customers.

## Solutions
NA

## Learnings
To prepare myself better have more questions regarding the employer/company like their product.

# Log 18-01-2023

## One Sentence summary of the day
Don't understand how to import the SSL Certificate and get it to work.

## Challenges
Find a way to import the Certificate.

## Solutions
After a talk with Casper I was pointed into the direction of SSL offloading. As well as understanding 
that I should make my search keywords more specific. Like what is really needed in this and anything that
is a maybe involved shouldn't be mentioned.

## Learnings
I understood that I should make my search keywords more specific, to get better search results that fit the question. Like what is really needed 
in this and anything that is a maybe involved shouldn't be mentioned.

# Log 19-01-2023

## One Sentence summary of the day

## Challenges

## Solutions

## Learnings
