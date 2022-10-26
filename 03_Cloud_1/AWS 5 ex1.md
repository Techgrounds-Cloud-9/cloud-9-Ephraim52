# Simple Storage Service (S3)
Learn to create your own buckets in S3 and how it works.

## Key terminology
AWS S3 4 storage classes defined:

S3 Standard - Frequently accessed data with low latency that makes it fast, reliable and durable to work with. Mostly used to store data for usage.

S3 Standard-IA - Infrequently accessed data with low latency that makes it fast, reliable and durable. This is also why it is a good storage class for long term storage like for disaster recovery to recover the backup.

S3 One-Zone IA - Infrequently accessed data and is a class that can be used to easily re-creatable data. This still has fast access due to low latency, but this data can be lost when the availability zone is destroyed.

S3 Glacier - Is a service for long term data archive digital preservation. Can be accessed quickly when retrieval is needed with the exception of the sub-classess, S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive, these take longer to retrieve due to the ability to retrieve data in bulk.

## Exercise
- Create new S3 bucket with the following requirements:
    - Region: Frankfurt (eu-central-1)
- Upload a cat picture to your bucket.
- Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.

### Sources
https://aws.amazon.com/s3/storage-classes/

My Word notes from the Cloud Practicioner Game at the Skill-Build website of Amazon.

### Overcome challenges
How to create a policy that allows access to the object(s) placed in the bucket for the public. I read that they have templates/examples of access policies and you need to put the lets say AWS object name/link in the policy to make it accessible. Once that was done I tested it with Elena and it worked, she could see the cat image.

### Results
Elena confirmed she could view the cat image through this link: https://mycat-jumping-now.s3.eu-central-1.amazonaws.com/New+Jumping+Cat.png

Bucket with the object which is a cat image.

![alt text]()

The policy in which you see the added AWS arn link to give access to the specific object for the public.

![alt text]()

The page where you could use the link for the object/image, which I send to Elena.

![alt text]()

The image displayed when the link is used.

![alt text]()
