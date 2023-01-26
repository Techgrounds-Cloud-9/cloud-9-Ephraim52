# Project V1.1 Documentation

This project has two versions v1.0 and v1.1. V1.0 is the basis required to build v1.1 on.

## Key terminology
Runtime error= Happens when attempted to run a program or code that functions/creates a program, yet has an error in the code that causes the crash when attempting to                run.

IndexError=The Python IndexError: list index out of range can be fixed by making sure 
           any elements accessed in a list are within the index range of the list. This can be 
           done by using the range() function along with the len() function.

class=Can be given any name just like a variable but between brackets needs to be defined what resource it needs to be. (Stack) or (Construct) these are examples there       are plenty more classes that can be defined.

parameter=You can set parameters by calling self.variable_name=which_resource you can use this to attach it to other resources outside the resource you defined this in.

def=Define the class for initiating the code with its variables, attributes, through scope, id, strings, keywordarguments or just arguments.

Ephemeral ports=

## Exercise
- For v1.0 I read the epics and filled it out in the requirements document.
- The same goes for v1.1 which I added in the same requirements document.
- Create a webserver and admin server to the specifics of the customer.

## Problems explained
### Setting parameters
In the stack you want to export the variable from. You define this variable between class and definition, like the kms_stack has "admin_key = kms.Key", 'kms' being the module and 'Key' being the class. Further down below in the stack you define the variable by writing it as such: self.admin_key=Admin_Key, this links the variable Admin_Key in the class key which creates a resource you want to export and use in another stack through the variable admin_key.

Then in the configuration file app.py import the stack and create a variable that calls the class of the stack (that being the stackname you imported). That being written as: "resource_encryption_Stack=KMS_stack(app, "kmsstack")", to export you also create a variable for the specific stack you want to import it to. "VPCStack_=VPCStack(app, "vpcstack", admin_server_enc_key=resource_encryption_Stack.admin_key)". What you see here is the variable VPCStack_ that respresents the class VPCStack importing through the resource_encryption_Stack variable the defined variable admin_key. Which is imported through the parameter admin_server_enc_key.

Then going to the VPCStack within define you set the construct_id (parameter) and the string (module and class attached to the variable in the parameter). Connect that parameter to the correct resource/part of your stack through another variable: kms_key=admin_server_enc_key.

### Getting the key from the Parameter store
Go to systems manager -> parameter store -> find the correct key ID through EC2 and check in the instance which key ID it is. Then go to the key in parameter store and show the content put that in a text file and convert it to a .pem file. This can be used for the RDP and SSH connection.

### SSH commandline
ssh -i "ec2-key-pair.pem" ec2-user@<Public IP or Private IP Webserver>

## Sources
Too many...

## Overcome challenges
Every error had to be solved one at a time. At some point I even remade my project v1.0.

## Results
Results will be shown in the presentation 27th of January 2023.
