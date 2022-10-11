# Asymmetric Encryption
This type of encryption uses two seperate yet mathematically connected cryptographic keys, called a public key and a private key. Together these are called a *Public and Private Key Pair*.
## Key terminology
- **Asymnmetric Key Systems**  
An asymmetric key system, also known as a public/private key system, uses two keys. The private key remains secret while the public key is made widely available to anyone who needs it. The private and public keys are mathematically tied together, so the corresponding private key can only decrypt that information encrypted using the public key.
- **Private Key**  
A private key, also known as a secret key, is a variable in cryptography that is used with an algorithm to encrypt and decrypt data. The private key is shared between the sender and receiver of data. In cybersecurity, an encryption key is a randomized string of bits used to encrypt and decrypt data. Each key is unique, and longer keys are harder to break. Typical key lengths are 128 and 256 bits for private keys and 2048 for public keys.
- **Public Key**  
See SEC-04.

## Exercise
### Sources
- https://cheapsslsecurity.com/blog/what-is-asymmetric-encryption-understand-with-simple-examples/  
- https://www.practicalnetworking.net/series/cryptography/using-asymmetric-keys/

### Overcome challenges
It required a bit of abstract thinking, how to send an encryption key on a public channel without others knowing what information is being sent.

### Results
- Daphne generated a key pair and proceeded to share the public key with us on Slack. Dominic and me used the same public key to encrypt our messages to Daphne, which we sent over Slack. She then proceeded to use her private key to decrypt our messages. In the next example Daphne=A and Dominic&Jaïr=B.
1. A generates a key-pair (public & private key)
2. A makes its public key public.
3. B encrypts the message with the public key.
4. B posts the encrypted message publicly.
5. A uses the private key to decrypt and read the message.
