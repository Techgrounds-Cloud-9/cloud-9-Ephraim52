# Detection, response and analysis
Understanding how detection, response and analysis come together in preventing an attack on a system.

## Key terminology
IDS= Intrusion detection systems this detects suspicious activities and sends alerts when they are detected.

IPS= Intrusion prevention systems is a tool this can be hardware or software it also monitors the network for suspicious activities and takes preventive actions. This can be reporting, blocking, dropping or a combination of them.

Systems hardening= This is a collection of tools that are used to reduce the security risk.

Automatic failover= Is a resource that a system admin can use like it says automatically switch the data handling to a standby system.

RPO= Recovery point objective is the maximum targeted period in which data is lost due to issues or incidents. In other words the actual data loss.

RTO= Recovery time objective stands for the 'real time' it takes to recover the system from the point of notification of the issue.

Zero-trust architecture= A structure within an organization where employees only get access to the data and systems they need for completing their work. This way attackers can't use the employees accounts because their access is limited to what they need to do.

Incident response plan= A plan of action on how to respond to each kind of incident, how to stop and recover from the incident.

WISP= Written information security plan, exists out of the policies & procedures on how data is to be protected. This plan helps the organization in its administration, but also on the technical part.

DDos= Distributed denial-of-service is an attempt to disrupt the normal traffic of IT systems by targetting the server, service or network by flooding the surrounding infrastructure connected to the targets.

Hot Site= A fully functional data center with personnel which is always up and operational in the event of a disaster.

Warm Site= A data center without customer data, a company/organization can install the needed equipment and customer data after a disaster. To limit the damage for the next occurence of the disaster.

Cold Site= Has the infrastructure to support the IT systems and data but is not active untill the company/organization is faced with a disaster. During the disaster it gets activated and can support a Hot and Warm site when faced with a long term disaster.

## Exercise
- A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
- An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?

### Sources
https://www.checkpoint.com/cyber-hub/network-security/what-is-an-intrusion-detection-system-ids/#:~:text=An%20Intrusion%20Detection%20System%20(IDS)%20is%20a%20monitoring%20system%20that,actions%20to%20remediate%20the%20threat.

https://www.vmware.com/topics/glossary/content/intrusion-prevention-system.html#:~:text=What%20is%20an%20intrusion%20prevention,it%2C%20when%20it%20does%20occur.

https://digitalguardian.com/blog/incident-response-plan

https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/#:~:text=A%20distributed%20denial%2Dof%2Dservice,a%20flood%20of%20Internet%20traffic.

https://www.eci.com/blog/16031-why-you-need-both-a-written-information-security-plan-and-a-business-continuity-plan.html#:~:text=What%20is%20a%20Written%20Information,your%20organization%20has%20in%20place.

https://www.beyondtrust.com/resources/glossary/systems-hardening

https://www.techopedia.com/definition/27075/automatic-failover

https://en.wikipedia.org/wiki/Disaster_recovery#Recovery_Point_Objective

https://www.druva.com/blog/understanding-rpo-and-rto/

https://securityboulevard.com/2019/11/5-tips-for-responding-to-cyber-attacks/

https://dynamixsolutions.com/types-disaster-recovery-plans/

https://bleuwire.com/strategies-cybersecurity-risk-mitigation/

https://blogs.tcsusa.com/4-incident-response-plan-strategies-for-your-business

https://www.msp360.com/resources/blog/how-to-respond-to-cyberattacks/

https://www.techtarget.com/searchdisasterrecovery/definition/disaster-recovery

### Overcome challenges
None encountered.

### Results
- The RPO is all the data lost between the point of Intrusion till where the intrusion is stopped. With all the data between the last backup and the point of when the incident occured.

- The RTO is the time where the incident occured till where the system is recovered. This is the eight minutes that were mentioned where the system is operational again.
