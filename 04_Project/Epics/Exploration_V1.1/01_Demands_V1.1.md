# What are the demands of the application?
On top of the old demands from V1.0:
- It should no longer be possible to approach the webserver "naked" over he internet. The customer would like to see a proxy installed. Additionally, the server should no longer have a public IP adress.
- If a user connects to the load balancer via HTTP, the connection should be automatically upgraded to HTTPS.
- In such an event, the connection should be encrypted by use of TLS 1.2 or higher.
- the webserver should be health checked in frequent intervals.
- Should the webserver fail this health check, than it should automatically be restored.
- If its the case that the webserver is placed under continuous load, a temporary extra server should be provisioned. The client thinks he will never need more than threee servers, given his past user numbers.