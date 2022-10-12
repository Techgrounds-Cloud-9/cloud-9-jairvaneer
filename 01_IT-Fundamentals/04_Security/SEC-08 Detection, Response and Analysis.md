# Detection, Response and Analysis
The three steps to follow when hit with a malware attack.
## Key terminology
- **Malware**  
Short for Malicious Software. It refers to all intrusive software developed by hackers to steal data and damage or destroy computers. Examples of common forms of malware are viruses, worms, Trojan viruses, spyware, adware, and ransomware.
- **Social Engineering**  
Social engineering is the art of manipulating people so they give up confidential information. 
- **IDS**  
Short for Intrusion Detection System. It is a device or piece of software that monitors a network for malicious activity or policy violations. ANy malicious activity is reported or collected using a SIEM system.  
- **SIEM**  
Short for Security Information and Event Management. It is a system combining Security Information Management (SIM) and Security Event Management (SEM) and it offers real-time monitoring and analysis of events as well as tracking and logging of security data for compliance or auditing purposes. It is a security solution that helps organizations recognize potential security threats and vulnerabilities before they have a chance to disrupt business operations. Most SOC's use this nowadays.
- **SOC**  
Short for Security Operation Center. It is a centralized function within an organization employing people, processes, and technology to continuously monitor and improve an organization's security posture while preventing, detecting, analyzing, and responding to cybersecurity incidents.
- **IPS**  
Short for Intrusion Prevention System. It is a network security tool (which can be a hardware device or software) that continuously monitors a network for malicious activity and takes action to prevent it, including reporting, blocking, or dropping it, when it does occur. It is more advanced than an IDS, which only detects, and therefore the more secure option.
- **Cold Backup**  
A type of back up which is done whan all users are offline. Cold backups are the safest way to backup data as no files can be changed during the backup. Cold backups can be performed on a copy of data too, such as that stored in an offsite repository. The benefit of cold backups is that the backup can’t be affected by live viruses or hacking attempts. They also won’t be affected by power surges, making them the most reliable way to backup your data. The downside is that during this time no users can access the system.
- **Hot Backup**  
A hot backup is performed whilst users are still logged into a system. The reason for performing hot backups is that it minimises downtime on a day-to-day basis, which is especially useful for systems that require 24/7 operation. The issue with hot backups is that if data is changed whilst the backup is being performed there may be some inconsistencies, such as the previous state of the file being included in the backup rather than the latest one. Hot backups also take up computer resources, so machine and server performance can be affected during backups.
- **Redundant Site**  
A redundant site maintains a live copy of all services running in real-time and is available instantly to ensure 100% server uptime. A redundant site should be entirely separate from your on-site server room and typically operates on a different network and service provider. This ensures that in the event of any single point of failure there is no interruption of services. The site would usually house an exact copy of any critical services and should be updated as frequently as possible.  
- **BCDR**  
Short for Business Continuity and Disaster Recovery. This is a plan that is implemented by businesses to ensure that they are prepared for IT disruptions that lead to sytems being down. The two most important parts of such a BCDR plan are the RPO and the RTO. 
- **RPO**  
Short for Recovery Point Objective. It  refers to the maximum acceptable amount of data loss measured in time. It marks the time during the disruption when the quantity of data lost exceeds the BCDR plan’s maximum allowable threshold. The purpose of RPO is to determine what the minimum backup schedule frequency is, how much data can be lost after a disaster, and how far back the IT admin team should go to employ sufficient restoration without delaying data loss against expected RTO.
- **RTO**  
Short for Recovery Time Objective. It refers to the quantity of time that an application, system and/or process, can be down for without causing significant damage to the business as well as the time spent restoring the application and its data. RTO measures the amount of downtime “tolerated” as per the BCDR plan. The purpose of RTO is to determine the real-time duration required to recover an asset (file/host/site) from the point in time the incident interrupts the normal flow of operations until restored. It also determines IT preparations for implementing the BCDR plan and the acceptable level of risk of data loss, when key 0systems or applications go offline.  
- **Disaster Recovery Options**  
These are the different options you have when setting up a BCDR, focusing on different types of business and different parts of the business. Such options include:  
*1. Data Back-Up Disaster Recovery Plans.* The most basic type of disaster recovery services you can use is for data back-up and recovery. All companies, no matter the size, need to have a complete copy of data stored offsite that can be restored in the case of an emergency. Its main features are using the 3-2-1 backup rule (keep 3 copies of your data of which 2 copies are on different backup mediums and 1 copy offsite), ensuring that backups are regularly monitored, testing data restoration regularly, backing up all devices (including smartphones and tablets) and backing up cloud services (Microsoft 365 etc.)   
*2. Virtual Disaster Recovery Plan.* This takes data back-ups a step further. Instead of only backing up your data, your entire IT infrastructure is backed up on cloud servers.
Features of the virtual disaster recovery plan include replication of your entire IT infrastructure (servers, storage, operating systems, software, apps, and data), use of virtual machines that allow your infrastructure to run from anywhere, operations are less reliant on hardware to run and the virtual environment can be restored to devices at any location.
*3. DRAAS (Disaster Recovery As A Service).* DRaaS is somewhat like a virtual disaster recovery plan, but in this case, everything is packaged and taken care of for you. You do not have to separately source backup applications or mitigation solutions, it’s all taken care of by the disaster recovery as a service provider.
DRaaS features a complete copy of your IT infrastructure in a 3rd party cloud environment. All verifications of backups and security are handled for you, and you don’t have to purchase any systems separately.
The benefits of using DRaaS include being able to focus completely on your business and knowing your operations are protected from natural disasters, equipment failures, and cyberattacks. 
*4. Hot Site Disaster Recovery.* For certain types of organizations, like medical facilities, nursing homes, and financial institutions, being down even for a few hours can be devastating. They can’t really afford any downtime as it will impact multiple other people that they serve. Hot site disaster recovery is a form of DRaaS that includes setting up a second physical facility filled with identical IT infrastructure. This is a higher cost but more complete protection from downtime. The benefit of setting up a “hot site” that you can use in the case of a disaster is that downtime can be nearly eliminated as the other site is on standby and ready to be used at any time. Data and devices have already been connected to the necessary systems and infrastructure are in place.
*5. Cold Stite Disaster Recovery.*
A slightly less-expensive alternative to a hot site is cold site disaster recovery. This involves renting space that can be used if needed. The space will already have servers and other infrastructure in place but won’t be set up and ready to go. The cold site takes a little longer to get up and running with your processes and data but offers an important alternate location to use if something happens to your physical location.
- **Automatic Failover**  
It is a resource that allows a system administrator to automatically switch data handling to a standby system in the event of system compromise. There are varioud
- **IR**
Short for Incident Report. In order to be able to respond to hacks, you need to develop an Incident Report (IR) plan. This consists of four steps: Preparation, Detection and Analysis, Containment, eradication and recovery, and Post-Incident Activity.  
*1. Preparation.*  Planning in advance how to handle and prevent security incidents.  
*2. Detection and analysis.* Encompasses everything from monitoring potential attack vectors to looking for signs of an incident, to prioritization.  
*3. Containment, eradication, and recovery.* Developing a containment strategy, identifying the hosts and systems under attack, mitigating the effects, and having a plan for recovery.  
***4. Post-incident activity.*** Reviewing lessons learned and having a plan for evidence retention.  
- **Hack Response Strategies**  
This pertains to how to respond to a cyber attack. The following steps should be taken:  
*1. Prevention.* The first step in responding to a successful cyberattack is to iterate the lessons you’ve learned from the recent attack back into your IR planning.  
*2. Communication and Delegation.*
Inform staff that an attack has occurred.Assemble a team that deals with responding to the incident.  
*3. Forensics.* This IR team should work to uncover the source of the attack or leak. This process is technically known as “attack forensics”, but in reality can be a lot less complex than that name suggests.
You should then immediately update how your phishing filters work in order to avoid the immediate reinfection of your systems.  
*4. Contain and Recover.* The next stage of incident response is to contain any further damage that might have been caused by a successful attack.  
*5. Stay Up-to-Date with All Your Security Systems.* It is pointless to have a security system in place that you won’t keep up-to-date.
*6. Assess the damage.* Take a full investigation into the damage.  
- **Systems Hardening**  
Systems hardening is a collection of tools, techniques, and best practices to reduce vulnerability in technology applications, systems, infrastructure, firmware, and other areas. The goal of systems hardening is to reduce security risk by eliminating potential attack vector s and condensing the system’s attack surface. By removing superfluous programs, accounts functions, applications, ports, permissions, access, etc. attackers and malware have fewer opportunities to gain a foothold within your IT ecosystem.  
Systems hardening demands a methodical approach to audit, identify, close, and control potential security vulnerabilities throughout B your organization. Nearly all layers of a system (see OSI Stack & TCP/IP, NTW-01 & NTW-02) can be hardened. 


## Exercise
### Sources
- https://www.cisco.com/c/en/us/products/security/advanced-malware-protection/what-is-malware.html  
- https://www.webroot.com/us/en/resources/tips-articles/what-is-social-engineering  
- https://www.barracuda.com/glossary/intrusion-detection-system  
- https://www.ibm.com/topics/siem  
- https://www.trellix.com/en-us/security-awareness/operations/what-is-soc.html  
- https://www.vmware.com/topics/glossary/content/intrusion-prevention-system.html#:~:text=What%20is%20an%20intrusion%20prevention,it%2C%20when%20it%20does%20occur  
-  https://vitanium.com/what-is-the-difference-between-hot-backup-and-cold-backup/  
- https://neucentrix.hk/the-importance-of-a-redundant-site-for-your-data/  
- https://www.acronis.com/en-us/blog/posts/rto-rpo/  
- https://www.unitrends.com/blog/rpo-rto  
- https://www.techopedia.com/definition/27075/automatic-failover
- https://www.beyondtrust.com/resources/glossary/systems-hardening  
- https://dynamixsolutions.com/types-disaster-recovery-plans/  
- https://www.msp360.com/resources/blog/how-to-respond-to-cyberattacks/  
- https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf

### Overcome challenges


### Results
- The RPO of the database of a company that makes daily backups of their database is determined by the time between back ups, as RPO is concerned with answering the question "Up to what point in time can the recovery process move tolerably, given the volume of data lost during that interval?". The company has decided that for them the loss of data up to one day old is tolerable, so their RPO is 24 hours. The time it takes to recover data lost up until the last back up is 15 minutes in this case, and that is their RTO.
- The RTO of a company that has an automatic failover to a back up server configured for their website is the length of the process it takes for the back up to be powered up and pull the newest version. In this case that is 8 minutes.