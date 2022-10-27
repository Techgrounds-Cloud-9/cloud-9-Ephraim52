# Elastic Block Store (EBS)
What is EBS & Snapshots and how to use them.

## Key terminology
For terminology please view AWS 4, 5 & 6!

Snapshot= A copy from a volume or instance that you can use as a backup to restore a lost volume or instance.

## Exercise 1
- Navigate to the EC2 menu.
- Create a t2.micro Amazon Linux 2 machine with all the default settings.
- Create a new EBS volume with the following requirements:
    - Volume type: General Purpose SSD (gp3)
    - Size: 1 GiB
    - Availability Zone: same as your EC2
- Wait for its state to be available.

## Exercise 2
- Attach your new EBS volume to your EC2 instance.
- Connect to your EC2 instance using SSH.
- Mount the EBS volume on your instance.
- Create a text file and write it to the mounted EBS volume.

## Exercise 3
- Create a snapshot of your EBS volume.
- Remove the text file from your original EBS volume.
- Create a new volume using your snapshot.
- Detach your original EBS volume.
- Attach the new volume to your EC2 and mount it.
- Find your text file on the new EBS volume.

### Sources
https://www.youtube.com/watch?v=pKA46UVy874

https://www.youtube.com/watch?v=vjyQwYml3Lg&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=32

### Overcome challenges
I tried creating the volume from the Snapshot using the snapshot id, thats when I saw an ongoing list of snapshot id's. Creating the volume from the snapshot this way didn't work in the volumes tab. So I tried creating the snapshot from the snapshot tab, there I selected my snapshot and went to actions to create a volume from the snapshot. This worked and I attached the snapshot to my instance and found the text file.

### Results
I created the EC2 instance.

![alt text]()

This is the EBS Volume I made.

![alt text]()

Attached the EBS Volume to the EC2 Instance.

![alt text]()

Logged in through SSH connection in Windows PowerShell.

![alt text]()

Before I mounted the EBS volume, I formatted the Virtual disk/EBS volume. Next was making a Path to mount the EBS volume to, as it cannot be the same as the root. Much like you have a hardware computer you cannot have two hard disks be master, there is always one master and the other hard disk is the slave drive.

So here you see that I formatted and mounted the EBS volume.

![alt text]()

Here you see the Volume is attached/mounted to the path of /mnt/ebsvolume.

![alt text]()

The next step was creating a text file with some content.

![alt text]()

This is the snapshot created from the volume.

![alt text]()

Remove the text file from the EBS volume.

![alt text]()

This is the volume created from the snapshot. The problem for creating this is described in the overcome challenges part.

![alt text]()

After that I detached the EBS volume and attached the volume created from the snapshot.

![alt text]()

Finally we arrived to the point where I had to search the test.txt file again and in this image you also see the content of the file.

![alt text]()