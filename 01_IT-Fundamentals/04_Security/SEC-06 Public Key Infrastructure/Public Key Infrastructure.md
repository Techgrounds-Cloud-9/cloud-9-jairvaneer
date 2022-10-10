# Public Key Infrastructure
 Public key infrastructure (PKI) is used to denote everything used to establish and manage public key encryption.

## Key terminology
- **PKI**  
Short for Public Key Infrastructure. It is a combination of authentication and encryption that makes secure online communication possible. As such, it's protocols are deployed in both web browsers and internal communications for organizations.  
- **Key**  
See SEC-04 and SEC-05.    
- **Digital Certificate**  
A document that acts as a digital passport, assigned to any entity that wants to participate in secure communication.  Secure connections between two communicating machines are made available through PKI because the identities of the two parties can be verified by way of these certificates. For internal communications you can create you own certifications, but for a website or organization, you need a CA.
- **CSR**  
Short for Certificate Signing Request. It is one of the first steps towards getting a SSL/TSL certificate. In this, all the information that is needed for the Certificate Authority (CA) to create your certificate is noted.  
- **CA**  
Short for Certificate Authority. This is a company or organization that acts to validate the identity of entities such as websites or users and bind them to cryptographic keys by issuing digital certificates such as SSL or TSL certificates.  
- **RA**  
Short for Registration Authority. This is a third-party that is authorized by the CA to provide digital certificates to users on a case-by-case basis. All of the certificates that are requested, received, and revoked by both the Certificate Authority and the Registration Authority are stored in an encrypted certificate database.
## Exercise
### Sources
- https://adamtheautomator.com/self-signed-certificates/  
- https://www.csoonline.com/article/3400836/what-is-pki-and-how-it-secures-just-about-everything-online.html  
- https://www.venafi.com/education-center/pki/how-does-pki-work#:~:text=What%20Are%20The%20Components%20Of,certificate%20authority%2C%20and%20registration%20authority  
- https://linuxize.com/post/creating-a-self-signed-ssl-certificate/  
- https://www.globalsign.com/en/blog/how-to-view-ssl-certificate-details  
- 

### Overcome challenges


### Results
- Created a Self-Signed SSL Certificate.