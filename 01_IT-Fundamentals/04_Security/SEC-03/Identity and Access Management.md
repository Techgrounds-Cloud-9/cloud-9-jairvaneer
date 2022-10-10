# Identity and Access Management
It's about ensuring that the right people and job roles in your organization (identities) can access the tools they need to do their jobs.
## Key terminology
- **IAM**  
Short for Identity and Access Management. It deals with ensuring that people and entities with digital identities have the right level of access to enterprise resources like networks and databases. User roles and access privileges are defined and managed through an IAM system.
- **Authentication**  
Authentication is the act of validating that users are whom they claim to be. This is the first step in any security process. There are a number of ways to do this:
1. Passwords. Usernames and passwords are the most common authentication factors. If a user enters the correct data, the system assumes the identity is valid and grants access.
2. One-time pins. Grant access for only one session or transaction.
3. Authentication apps. Generate security codes via an outside party that grants access.
4. Biometrics. A user presents a fingerprint or eye scan to gain access to the system. 
- **Authorization**  
Authorization in system security is the process of giving the user permission to access a specific resource or function. This is also called *access control* or *client privilege*. In secure environments, authorization must always follow authentication. Users should first prove that their identities are genuine before an organization’s administrators grant them access to the requested resources.
- **MFA**  
Short for Multi-Factor Authentication. Sometimes systems require the successful verification of more than one factor before granting access. This multi-factor authentication requirement is often deployed to increase security beyond what passwords alone can provide.


## Exercise
### Sources
- https://www.okta.com/identity-101/authentication-vs-authorization/#:~:text=Authentication%20confirms%20that%20users%20are,and%20access%20management%20(IAM)  
- https://www.cisco.com/c/en/us/products/security/identity-services-engine/what-is-identity-access-management.html
- https://rublon.com/blog/what-are-the-three-authentication-factors/  
- https://www.cisa.gov/uscert/bsi/articles/knowledge/principles/least-privilege#:~:text=The%20Principle%20of%20Least%20Privilege%20states%20that%20a%20subject%20should,control%20the%20assignment%20of%20rights 


### Overcome challenges


### Results
- Studied the difference between authentication and authorization. Authentication confirms that users are who they say they are. Authorization gives those users permission to access a resource.
- Studied the three factors of authentication and how MFA improves security. An authentication factor is a category of evidence that a person has to present to prove they are who they say they are. The three factors are:
1. The Knowledge Factor: This pertains to something you know, like a password.
2. The Possession Factor: This pertains to a physical item that you have, like a mobile phone.
3. The Inherence Fcator: This pertains to something you are, like a fingerprint.  
By requiring proof of authentication by use of two of these factors you greatly increase the chance that someone is who they say they are.
- Studied the principle of least privilege and how it improves security. The principle of least privilege states that a subject should be given only those privileges needed for it to complete its task. If a subject does not need an access right, the subject should not have that right. Further, the function of the subject (as opposed to its identity) should control the assignment of rights. By not having access to things that the user does not need, you improve security.
