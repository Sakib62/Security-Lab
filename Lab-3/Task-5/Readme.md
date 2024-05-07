# Task - 5 : Generating Message Digest

Following steps are followed to generate hash value of a file:

1. Create a text file and add some text. I named it [text.txt](text.txt)
2. Use the `SHA-256` (Secure Hashing Algorithm) hashing algorithm by the following command:

    ```
    openssl dgst -sha256 text.txt
    ```
    
    Generated Hash:
    
    ```
    2862d2fda986953340b9ad696afb168a6bd02eaa04efaea80452278f5852d416
    ```
3. Use the `SHA-1` hashing algorithm by the following command:
    ```
    openssl dgst -sha1 text.txt
    ```

    Generated Hash:

    ```
    8f0e7d6587f3d754343ead29c2115174891a6c1e
    ```
4. Use the `MD-5` (Message Digest) hashing algorithm by the following command:

    ```
    openssl dgst -md5 text.txt
    ```

    Generated Hash:

    ```
    4ef7690f6ba6af63db4de8e29da21bd9
    ```
### Observations

1. **SHA-256**
    - Produces longer hash value (256bit, 32-byte) compared to MD5 and SHA-1.
    - Provides better security against collisions and widely used in modern cryptographic application including digital signatures, certificate authorities, password hashing, and blockchain technology.
2. **SHA-1**
    - Produces 160 bit (20 byte) hash value.
    - Considered weak and vulnerable to collision attacks.
3. **MD5**
    - Produces 128 bit (16 byte) hash value.
    - Fast and commonly used for checksums and data integrity verification.
    - Vulnerable to collision attacks.

So, `SHA-256 is the most secure one.` MD5, thought fast, considered insecure. SHA-1 is stronger than MD5 but also vulnerable to collision attacks and less secure than SHA-256.
