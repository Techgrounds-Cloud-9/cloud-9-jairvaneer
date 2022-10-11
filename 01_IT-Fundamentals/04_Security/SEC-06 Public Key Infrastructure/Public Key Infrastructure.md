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
- **Certification Path**  
A chain of trusted public-key certificates that enables the receiver to verify that the sender and all intermediate certificates are trustworthy. Each certificate in the path must have been signed by the private key corresponding to the public key contained in the certificate that precedes it in the path, and the first certificate in the path must have been issued by a Trust anchor.
## Exercise
### Sources
- https://adamtheautomator.com/self-signed-certificates/  
- https://www.csoonline.com/article/3400836/what-is-pki-and-how-it-secures-just-about-everything-online.html  
- https://www.venafi.com/education-center/pki/how-does-pki-work#:~:text=What%20Are%20The%20Components%20Of,certificate%20authority%2C%20and%20registration%20authority  
- https://linuxize.com/post/creating-a-self-signed-ssl-certificate/  
- https://www.globalsign.com/en/blog/how-to-view-ssl-certificate-details  
- https://csrc.nist.gov/glossary/term/certification_path  
- http://woshub.com/updating-trusted-root-certificates-in-windows-10/
- https://www.globalsign.com/en/blog/how-to-view-ssl-certificate-details
- https://documentation.observeit.com/installation_guide/finding_the_path_to_the_trusted_certificates.htm


### Overcome challenges


### Results
- Created a Self-Signed SSL Certificate. ![Certificate VM](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/c6b06ab972c5923c20c742c6c0ca056533f07c8a/00_includes/Sprint%202/Screenshots%20Security/SEC-06%20Public%20Key%20Infrastructure/SEC-06%20Exercise%201%20-%20%231_New_Certificate_%20VM.png)  ![Certificate output](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2de750025813d8de58dc53b292edac7e954c9410/00_includes/Sprint%202/Screenshots%20Security/SEC-06%20Public%20Key%20Infrastructure/SEC-06%20Exercise%201%20-%20%232_New_Certificate_%20VM_2.png)
- Analyzed the certification paths of google.com and techgrounds.nl. ![google certificate](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/4cbd0e8bd5d70e351731360afd13ec1bc62dc6e5/00_includes/Sprint%202/Screenshots%20Security/SEC-06%20Public%20Key%20Infrastructure/SEC-06%20Exercise%201%20-%20%232_Google_Certificate_Path_1.png) ![google certificate 2](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/4cbd0e8bd5d70e351731360afd13ec1bc62dc6e5/00_includes/Sprint%202/Screenshots%20Security/SEC-06%20Public%20Key%20Infrastructure/SEC-06%20Exercise%201%20-%20%233_Google_Certificate_Path_2.png) ![techgrounds certificate](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/4cbd0e8bd5d70e351731360afd13ec1bc62dc6e5/00_includes/Sprint%202/Screenshots%20Security/SEC-06%20Public%20Key%20Infrastructure/SEC-06%20Exercise%201%20-%20%234_Techgrounds_Certificate_Path.png)
- Found the list of trusted certificate roots on my system in two ways; by using the CLI and the GUI. ![CLI](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2de750025813d8de58dc53b292edac7e954c9410/00_includes/Sprint%202/Screenshots%20Security/SEC-06%20Public%20Key%20Infrastructure/SEC-06%20Exercise%201%20-%20%236_Trusted_Root_Certificates_Local_Machine_Terminal.png) ![GUI](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2de750025813d8de58dc53b292edac7e954c9410/00_includes/Sprint%202/Screenshots%20Security/SEC-06%20Public%20Key%20Infrastructure/SEC-06%20Exercise%201%20-%20%237_Trusted_Root_Certificates_Local_Machine.png)
- Also found the list in my VM. ![VM Certificates](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/6700eab2eac77db94e6ddb4661211196598b88dc/00_includes/Sprint%202/Screenshots%20Security/SEC-06%20Public%20Key%20Infrastructure/SEC-06%20Exercise%201%20-%20%238_Trusted_Root_Certificates_VM.png)