# Passwords
Where and how passwords are stored on your computer, and how these are protected from hackers.

## Key terminology
- **Passwords**  
 A password is a string of characters used to verify the identity of a user during the authentication process. It falls in the 'something you know'category of authentication.
- **Password Manager**  
A password manager is a software application designed to store and manage online credentials. It also generates passwords. Usually, these passwords are stored in an encrypted database and locked behind a master password.
- **Hashing**   
Hashing is the process of converting a given key into another value. A hash function is used to generate the new value according to a mathematical algorithm. The result of a hash function is known as a hash value or simply, a hash. A good hash function uses a one-way hashing algorithm, or in other words, the hash cannot be converted back into the original key. Whenever a user enters a password, it is converted into a hash value and is compared with the already stored hash value. If the values match, the user is authenticated.
- **Rainbow Table**  
A rainbow table is a database that is used to gain authentication by cracking the password hash. It is a precomputed dictionary of plaintext passwords and their corresponding hash values that can be used to find out what plaintext password produces a particular hash. Since more than one text can produce the same hash, it’s not important to know what the original password really was, as long as it produces the same hash.
- **Salting**
Salting is the process of adding unique random strings of characters to passwords in a database or each password before the password is hashed (a term we'll come back to). This is done to change the hash and make passwords more secure. The string of characters added to the password is called the salt. A salt can be added in front or behind a password. The salt is not made public and is known to only the site.
## Exercise
### Sources
- https://www.malwarebytes.com/what-is-password-manager#:~:text=A%20password%20manager%20is%20a,locked%20behind%20a%20master%20password  
- https://www.educative.io/answers/what-is-hashing  
- https://www.geeksforgeeks.org/understanding-rainbow-table-attack/  
- https://www.makeuseof.com/what-is-salting/  
- https://www.baeldung.com/cs/hashing-vs-encryption

### Overcome challenges


### Results
- Hashing is the process of converting a given key to another value. It is therefore a manner of encrypting. However, it is preferred to symmetric encryption for storing passwords as it is non-reversable. It uses a one-way hashing algorithm, meaning that the hash caannot be converted to the original plaintext key. Symmetric encryption uses the same key for encrypting and decrypting the data, meaning that the encrypted password can be decrypted if someone possesses the key. Therefore, hashing is more secure and thus preferred over symmetric encryptioon for storing passwords.  
- A rainbow table works by doing a cryptanalysis very quickly and effectively. Hackers must first gain access to leaked hashes in order to carry out rainbow table attacks. Once they have the password hashes and know what type of hash algorithm is used the rainbow table is used to help decrypt the password hashes.  
A rainbow table for a hashing algorithm holds all the hashes for any number of plaintext values that can be used as a password. By hashing and rehashing a plaintext string a chain of plaintext string hashes is created, that spans from the first plaintext to the last hash. When enough of these chains are produced, they are stored in a table. Starting off with the hashed text (the password) its checked if it exists in the database. If so, go to the start of the chain and start hashing until there is a match. As soon as the match is obtained, the process ceases and the authentication is cracked.  
![flowchart rainbow table](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/9912fedc3db5058d841736485f87a1676c35ca40/00_includes/Sprint%202/Screenshots%20Security/SEC-07%20Passwords/SEC-07%20Exercise%201%20-%20%231_How_Rainbow_Table_Works.png)
- 
