# Simple Storage Service (S3)
Learn to create your own buckets in S3 and how it works.

## Key terminology
AWS S3 4 storage classes defined:

S3 Standard - Frequently accessed data with low latency that makes it fast, reliable and durable to work with. Mostly used to store data for usage.

S3 Standard-IA - Infrequently accessed data with low latency that makes it fast, reliable and durable. This is also why it is a good storage class for long term storage like for disaster recovery to recover the backup.

S3 One-Zone IA - Infrequently accessed data and is a class that can be used to easily re-creatable data. This still has fast access due to low latency, but this data can be lost when the availability zone is destroyed.

S3 Glacier - Is a service for long term data archive digital preservation. Can be accessed quickly when retrieval is needed with the exception of the sub-classess, S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive, these take longer to retrieve due to the ability to retrieve data in bulk.

ARN= A unique identifier for your resource on Amazon (AWS).

Website Endpoint= This is a web service URL/link that allows users to access a specific service this endpoint represents the connection point where the html files are exposed as a website. (html is used to build websites through code instead of fixed templates.)

## Exercise
- Create new bucket with the following requirements:
    - Region: Frankfurt (eu-central-1)
- Upload the four files that make up AWS’ demo website.
- Enable static website hosting.
- Share the bucket website endpoint with a peer. Make sure they are able to see the website.

### Sources
https://aws.amazon.com/s3/storage-classes/

https://www.youtube.com/watch?v=KASOBo_8Py0

https://www.biztalk360.com/blog/web-endpoint-monitoring-biztalk360/#:~:text=In%20simple%20terms%2C%20a%20web,active%20server%20pages%20are%20exposed.

My Word notes from the Cloud Practicioner Game at the Skill-Build website of Amazon.

### Overcome challenges
For the first exercise I realized now that you could simply make the objects public through the actions menu when you are viewing/selecting the objects. Although this didn't work for the settings I used I made my own access policy again.

### Results
Created the Bucket with the required Objects inside.

![alt text]()

I had to set the Access Policy again as shown in exercise 1 of this assignments. Which I also refer to for viewing this part of the exercise.

After uploading the Objects I created the Static Website Hosting, where the endpoint is created after setting the settings.

![alt text]()

This is what my peer saw.

![alt text]()
