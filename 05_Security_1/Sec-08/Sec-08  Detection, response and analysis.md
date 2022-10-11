# Detection, response and analysis
Understanding how detection, response and analysis come together in preventing an attack on a system.

## Key terminology
IDS= Intrusion detection systems this detects suspicious activities and sends alerts when they are detected.

IPS= Intrusion prevention systems is a tool this can be hardware or software it also monitors the network for suspicious activities and takes preventive actions. This can be reporting, blocking, dropping or a combination of them.

Systems hardening= This is a collection of tools that are used to reduce the security risk.

Automatic failover= Is a resource that a system admin can use like it says automatically switch the data handling to a standby system.

RPO= Recovery point objective is the maximum targeted period in which data is lost due to issues or incidents. In other words the actual data loss.

RTO= Recovery time objective stands for the 'real time' it takes to recover the system from the point of notification of the issue.

## Exercise
- A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
- An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?

### Sources
https://www.checkpoint.com/cyber-hub/network-security/what-is-an-intrusion-detection-system-ids/#:~:text=An%20Intrusion%20Detection%20System%20(IDS)%20is%20a%20monitoring%20system%20that,actions%20to%20remediate%20the%20threat.

https://www.vmware.com/topics/glossary/content/intrusion-prevention-system.html#:~:text=What%20is%20an%20intrusion%20prevention,it%2C%20when%20it%20does%20occur.

https://www.beyondtrust.com/resources/glossary/systems-hardening

https://www.techopedia.com/definition/27075/automatic-failover

https://en.wikipedia.org/wiki/Disaster_recovery#Recovery_Point_Objective

https://www.druva.com/blog/understanding-rpo-and-rto/

https://securityboulevard.com/2019/11/5-tips-for-responding-to-cyber-attacks/

https://dynamixsolutions.com/types-disaster-recovery-plans/

### Overcome challenges
None encountered.

### Results
- The RPO is all the data lost between the point of Intrusion till where the intrusion is stopped. With all the data between the last backup and the point of when the incident occured.

- The RTO is the time where the incident occured till where the system is recovered. This is the eight minutes that were mentioned where the system is operational again.
