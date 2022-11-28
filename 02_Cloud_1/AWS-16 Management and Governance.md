# Management and Governance  
A collection of services that AWs offers to clients so they can control cost, compliance and security as well as continue to innovate. These services improve business agility and governance control.
## Key terminology
- **AWS Config**    
AWS Config continually assesses, audits, and evaluates the configurations and relationships of your resources. The client can set configuration rules with which the AWS resources should comply, and track whether the resources comply with those rules.  Every time a resource is changed, Config records the change in an S3 bucket. It stores a snapshot of the system at a regular period of time set by you, and even records how one AWS resource relates to another. It stores a configuration history in S3, and presents an overview of your resources and their configurations in a dashboard.  
You can integrate Config with IAM to set permissions for what a user can or cannot do within a resource.
- **AWS Cloudtrail**  
AWS CloudTrail monitors and records account activity across your AWS infrastructure, giving you control over storage, analysis, and remediation actions. CloudTrail is a logging service that records all API calls to any AWS service. It records details of the call like which user or application made the call, when it was made, and what IP address it was made from. It is a web service, meaning it is a software system that supports machine-to-machine interaction, in this case, the monitoring and recording of activity.
AWS also has another logging service called CloudWatch Logs, but this reports application logs, unlike CloudTrail which reports on how AWS services are being used.  
Though they often report on the same incidents, their perspective and approach is different. Config reports on what has changed, whereas CloudTrail reports on who made the change, when, and from which location. Config is focused on the configuration of your AWS resources and reports with detailed snapshots on how your resources have changed. CloudTrail focuses on the events, or API calls, that drive those changes. It focuses on the user, application, and activity performed on the system.  
Cloudtrail integrates with CloudWatch Events to allow you to set automated rules-based responses to any event that occurs in your resources.
- **API**  
Short for Application Programming Interface.  In the context of APIs, the word Application refers to any software with a distinct function. Interface can be thought of as a contract of service between two applications. This contract defines how the two communicate with each other using requests and responses. Their API documentation contains information on how developers are to structure those requests and responses.
- **AWS Cloudwatch**  
Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance. You can use this to set alarms when certain thresholds are reached or crossed, and automate the appropriate response to these events.  
You can configure CloudTrail with CloudWatch Logs to monitor your trail logs and be notified when specific activity occurs using the Amazon Simple Notification Service (SNS). You can also configure CloudWatch to automatically perform an action in response to an alarm.


## Exercise
### Sources
- https://aws.amazon.com/products/management-and-governance/  
- https://aws.amazon.com/config/?c=mg&sec=srv  
- https://aws.amazon.com/cloudtrail/?c=mg&sec=srv  
- https://aws.amazon.com/cloudwatch/?c=mg&sec=srv  
- https://www.sumologic.com/blog/aws-config-vs-cloudtrail/  
- http://www.adibitech.com/aws-config-vs-trusted-advisor-vs-cloudtrial/#:~:text=The%20recommendation%20provided%20by%20trusted,the%20AWS%20infrastructure%20more%20robust.&text=AWS%20Config%20allows%20to%20review,the%20organization%20and%20change%20management  
- https://aws.amazon.com/what-is/api/  
- https://www.opsramp.com/guides/aws-monitoring-tool/cloudtrail-vs-cloudwatch/#:~:text=CloudWatch%20is%20a%20monitoring%20service,activity%20in%20your%20AWS%20account.&text=CloudWatch%20monitors%20applications%20and%20infrastructure,actions%20in%20the%20AWS%20environment  


### Overcome challenges


### Results
- Connected a CLoudwatch alarm to a new EC2 instance, which would stop the instance when the average CPU usage reached above a certain level (0.2%).
- Learned about AWS Management tools.