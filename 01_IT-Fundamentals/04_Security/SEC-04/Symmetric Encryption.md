# Symmetric Encryption
 A style of encryption that uses a single key to encrypt and decrypt.
## Key terminology
- **Symmetric Encryption**  
Symmetric encryption uses a single key to encrypt and decrypt. This is also called “secret key” encryption because the key must be kept secret from others. It is a fast encryption way, however, the key must be shared beforehand between parties.
- **Cipher**  
A system for encrypting and decrypting data. It is also called an algorithm and contains the rules or instructions for the encryption process. The key length, functionality, and features of the encryption system in use determine the effectiveness of the encryption. By use of a key, the cipher encrypts plaintext into ciphertext, whereafter only those with the decryption key can reverse the process and read the original plaintext message. There are four categories of ciphers:  
**1. Block Ciphers.** These accumulate symbols in a message of a fixed size, which is called the block.  
**2. Stream Ciphers.** These work on a continuous stream of symbols.  
**3. Symmetric Key Algorithms.** A style of encrypting that uses a single key to encrypt and decrypt.  
**4. Asymmetric key algorithms.** A style of encryption that uses a different key for encryption and decryption.
- **Plaintext & Ciphertext**  
Plaintext is the original message that is being communicated between two parties. Ciphertext is that same message, but encrypted, by use of a cipher and a key.  
- **Symmetric Key System**  
In a symmetric key system, everyone accessing the data has the same key. Keys that encrypt and decrypt messages must also remain secret to ensure privacy. While it's possible for this to work, securely distributing the keys to ensure proper controls are in place makes symmetric encryption impractical for widespread commercial use.  
- **Asymnmetric Key Systems**  
SEE SEC-5..
- **Private Key**  
See SEC-05.
- **Public Key**  
A variable used in cryptography to encrypt data. A public key may be used by anyone, but only the entity that holds the correct private key that is linked to a message can decrypt that message again. 
- **SSL**  
Short for Secure Sockets Layer. It is an encryption protocol and the standard technology used in keeping an internet connection secure and for the protection of data between tow (or more) systems. In order to use this, a website needs to have an added SSL certificate, a digital certificate that authenticates the website's identity and enables an encrypted connection.
- **TLS**  
Short for Transport Layer Security. This is the improved and more secure version of SSL. Nowadays, when a website has a SSL certificate, in most cases this is a TSL certificate, but SSL is still widely applied as name because it is so well-known. 
- **CSR**  
Short for Certificate Signing Request. It is one of the first steps towards getting a SSL/TSL certificate. In this, all the information that is needed for the Certificate Authority (CA) to create your certificate.  
- **CA**  
Short for Certificate Authority. This is a company or organization that acts to validate the identity of entities such as websites or users and bind them to cryptographic keys by issuing digital certificates such as SSL or TSL certificates.  
- **Certificate**  
A document that acts as a digital passport, assigned to any entity that wants to participate in secure communication.

## Exercise
### Sources
- https://www.sciencedirect.com/topics/computer-science/symmetric-encryption#:~:text=Symmetric%20encryption%20uses%20a%20single,kept%20secret%20from%20third%20parties  
- https://www.hypr.com/security-encyclopedia/cipher  
- https://www.networking4all.com/nl/helpdesk/faq/wat-is-een-private-key-en-public-key  
-https://www.kpn.com/zakelijk/blog/ssl-tls-https.htm  
- https://www.kaspersky.com/resource-center/definitions/what-is-a-ssl-certificate  
- https://www.ssl.com/faqs/what-is-a-certificate-authority/  
- https://www.arcserve.com/blog/5-common-encryption-algorithms-and-unbreakables-future

### Overcome challenges


### Results
- Two historic ciphers beside the Caesar cipher are:  
**1. The Vigenère Cipher.** A Vigenère cipher uses a table consisting of different Caesar shifts in sequence and a key to encode a message across several rows of the table. By using different Caesar shifts for different characters in the message, the Vigenère cipher makes decoding the ciphertext using frequency analysis much more difficult.  
**2. The book cipher.** This is an encryption method where both the sender and recipient of a secret message must have the same copy of a book, usually down to the same edition. The sender then encodes the secret message word-by-word by replacing the plaintext word with coordinates mapping to the location of the same word within the chosen book. 
- Two digital ciphers that are being used today are:  
**1. AES.** Short for Advanced Encryption Standard. This algorithm is trusted as the standard by the U.S. Government and numerous organizations. It uses most commonly an 128-bit form but also keys of 192 and 256 bits for heavy-duty encryption purposes.
AES is largely considered impervious to all attacks, except for brute force, which attempts to decipher messages using all possible combinations in the 128, 192, or 256-bit cipher.  
**2. RSA Security.** This is a public-key encryption algorithm and the standard for encrypting data sent over the internet. It uses a public key to encrypt and a private key to encrypt, making it an asymmetric key system.  
- The biggest disadvantage of symmetric encryption is its use of a single cryptographic key to encrypt and decrypt information.