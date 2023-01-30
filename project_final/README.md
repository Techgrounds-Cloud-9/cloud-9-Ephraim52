
# Welcome to your project_final!

1.  Create 2 VPC's in your nearest region (eu-central-1) within this you have availability zones where your subnets reside.
    The VPC's having the CIDR-blocks 10.10.10.0/24 (webserver) & 10.20.20.0/24 (admin server). Everything can be configured
    if you change the region and AZ's in the code.
2.  The Webserver vpc is stretched over three availability zones with a public subnet with CIDR mask 28 and a private subnet 
    with CIDR mask 26. For a private subnet to have access to the internet it needs an NAT Gateway which is provided.
3.  The Admin vpc has a public subnet and stretches two availability zones with a CIDR mask 25.
4.  Autoscaling Group replaces the original EC2 Webserver and provides a backup through the AMI as long as there is no data
    stored on the Webserver. The Webserver uses Linux OS on the private subnets and if needed a backup vault can be created
    to store data that is being used on the webserver.
5.  The other is an EC2 Instance that provides the Admin server which uses Windows 2022 OS. It serves as a host to get to the
    Webserver.
6.  Keys are being created in KMS which are used for the encryption of the Webserver and Admin server. For their EBS Volumes
7.  All subnets are protected by their respective Nacl's for their specific required inbound and outbound traffic rules.
8.  The VPC peering connection connects the two servers by taking their CIDR-blocks of the VPC. To connect everything together
    as the subnets are stretched over multiple availability zones and each provides for a server (EC2 Instance).
9.  The EC2 Instances are protected by the Security groups which only provides the required inbound traffic rules and allows
    all outbound rules.
10. The S3 Bucket provides a storage from where the Webserver (EC2 Instance) can get the userdata(bash script) that needs to 
    be uploaded and then downloaded to the server. 
11. A Load balancer is added to act as a proxy for incoming traffic and divide this, the initial idea was to have an SSL 
    Certificate. This way you would be able to redirect traffic from HTTP to HTTPS which is secured through TLS 1.2 with the 
    SSL Certificate.
12. Only the trusted ip refered to the variable my_ip which can contain ip address you trust has the ability to make the RDP 
    with the admin server and the SSH connection with the webserver.
13. Some IAM roles have been created to provide only access to the resources required to function.


# How to use the CDK Toolkit
Before getting started a couple of programs need to be installed.
- So install AWS CLI on your device, from the: https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html
- If you have an AWS account create in the IAM a user and get the Access key ID, Secret key ID for the AWS user. You will use this to set up the environment, don't get these credentials directly from the root user. Also give the user you created full Administrative Permissions.
- The next step is configuring the user and you can login using:
```
aws configure
```

- The following options should come up in consecutive order.

```
AWS Access Key ID [None]: <type key ID here>
AWS Secret Access Key [None]: <type access key>
Default region name [None]: <choose region (e.g. "us-east-1", "eu-west-1")>
Default output format [None]: <leave blank>
```

- After this install node.js which you can download here -> https://nodejs.org/en/
- If you already have node.js check the version if it is up to date with:
```
node --version
```
- Make sure you have an Integrated Development Environment (IDE) install something like VScode: https://code.visualstudio.com/
- Next step is installing the AWS CDK Toolkit, within the IDE open a terminal and enter the following command: (In some cases you might need to use 'sudo' infront of the command)
```
npm install -g aws-cdk
```
- Install Python and set it to the PATH of your environment. Download the installer from: https://www.python.org/downloads/

# How to use your CDK environment
- Create a folder/directory in which you will initiate the environment and download the files in using:
```
mkdir cdk_workshop && cd cdk_workshop
```
- Next we will start to download the required files for the environment. Which will be made in the programming language you specify below by using:
```
cdk init sample-app --language python
```
- Start here if you have the app.
- Then we can create the Python virtual environment in this directory we created using the command:
```
python -m venv .venv
```
- To activate your environment you can use different commands depending on which OS you are using. For UNIX-based systems:
```
source .venv/bin/activate
```
For Windows OS:
```
.venv\Scripts\activate.bat
```
Although these worked for me as well on Windows:
```
.venv\Scripts\activate
```
Or:
```
.venv\Scripts\activate.ps1
```

- When the environment is active you can install the requirements by using:
```
pip install -r requirements.txt
```
- Now you can Synthesize your environment to generate a CloudFormation Template of the environment using:
```
cdk synth
```
- To upload your stacks, app, work you need to use bootstrap. This way CloudFormation can create the infrastructure from the stacks, etc.
```
cdk bootstrap
```
- To check your work/app for any errors and to make sure it is fine use:
```
cdk ls
```
- This will either give you a list of errors, showing lines where to troubleshoot. Or show you that everything is fine with the code like this:
```
kmsstack
vpcstack
NaclStack
webasgalbstack
``` 
- Later on when you feel like testing the functionality you can deploy it using:
```
cdk deploy (insert stackname)
```
- Or if you use multiple stacks like my example you need to use this command:
```
cdk deploy --all
```
To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
