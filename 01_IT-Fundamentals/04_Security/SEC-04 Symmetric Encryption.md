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


## Exercise
### Sources
- https://www.sciencedirect.com/topics/computer-science/symmetric-encryption#:~:text=Symmetric%20encryption%20uses%20a%20single,kept%20secret%20from%20third%20parties  
- https://www.hypr.com/security-encyclopedia/cipher  
- https://www.networking4all.com/nl/helpdesk/faq/wat-is-een-private-key-en-public-key  
-https://www.kpn.com/zakelijk/blog/ssl-tls-https.htm  
- https://www.kaspersky.com/resource-center/definitions/what-is-a-ssl-certificate  
- https://www.ssl.com/faqs/what-is-a-certificate-authority/  
- https://www.arcserve.com/blog/5-common-encryption-algorithms-and-unbreakables-future
- https://www.techrepublic.com/article/solving-the-key-exchange-problem/  
- https://www.practicalnetworking.net/series/cryptography/symmetric-encryption/  
- https://www.dcode.fr/caesar-cipher  
- https://travistidwell.com/jsencrypt/demo/  

### Overcome challenges
It took some time to figure out that the only way to do this was to use a hybrid encryption method, but once we figured that out by working on SEC-05, it went fast.

### Results
- Two historic ciphers beside the Caesar cipher are:  
**1. The Vigenère Cipher.** A Vigenère cipher uses a table consisting of different Caesar shifts in sequence and a key to encode a message across several rows of the table. By using different Caesar shifts for different characters in the message, the Vigenère cipher makes decoding the ciphertext using frequency analysis much more difficult.  
**2. The Book Cipher.** This is an encryption method where both the sender and recipient of a secret message must have the same copy of a book, usually down to the same edition. The sender then encodes the secret message word-by-word by replacing the plaintext word with coordinates mapping to the location of the same word within the chosen book. 
- Two digital ciphers that are being used today are:  
**1. AES.** Short for Advanced Encryption Standard. This algorithm is trusted as the standard by the U.S. Government and numerous organizations. It uses most commonly an 128-bit form but also keys of 192 and 256 bits for heavy-duty encryption purposes.
AES is largely considered impervious to all attacks, except for brute force, which attempts to decipher messages using all possible combinations in the 128, 192, or 256-bit cipher.  
**2. RSA Security.** This is a public-key encryption algorithm and the standard for encrypting data sent over the internet. It uses a public key to encrypt and a private key to encrypt, making it an asymmetric key system.  
- We used what is called a hybrid encryption, where we use the same (symmetrical) key to encrypt and decrypt our messages, but an asymmetrical key to encrypt the key. For the messages I used a Caesar Cipher with a shift of 10 to encrypt the message. Then Daphne sent me her RSA Public Key, which I used to encrypt the message ***Caesar Cipher Shift 10***.  Then I sent this to her, so that she would know the cipher and the key which we used to encrypt and decrypt our messages. I sent her the message ***XUBBE WYJKF***, which when decrypted using the right cipher and key reads ***Hello Gitup*** (our group name). ![encryption being send](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/25027df9b44b1042026a2ff3fa45bca94c4084a8/00_includes/Sprint%202/Screenshots%20Security/SEC-04%20Symmetric%20Encryption/SEC-04%20Exercise%201%20-%20%231_Symmetric_Key_Exchange.png)  
![caesar cipher](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/25027df9b44b1042026a2ff3fa45bca94c4084a8/00_includes/Sprint%202/Screenshots%20Security/SEC-04%20Symmetric%20Encryption/SEC-04%20Exercise%201%20-%20%232_Screenshot_Caesar_Key.png)  
![Solution cipher](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/25027df9b44b1042026a2ff3fa45bca94c4084a8/00_includes/Sprint%202/Screenshots%20Security/SEC-04%20Symmetric%20Encryption/SEC-04%20Exercise%201%20-%20%233_Screenshot_Caesar.png)
- The biggest disadvantage of symmetric encryption is its use of a single cryptographic key to encrypt and decrypt information. This creates the need of sending the key to the other party which is a lot less secure than a asymmetrical encryption, where only the encryption key is shared but not the decryption key.