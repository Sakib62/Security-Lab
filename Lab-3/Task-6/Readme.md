# Task - 6 : Keyed hash and HMAC

The following steps are followed to generate Keyed Hash and HMAC:

1. Create a text file and add some text. I named it [text.txt](text.txt)
2. Generate a keyed hash using `HMAC-MD5` algorithm by the following command
    ```
    openssl dgst -md5 -hmac "key for hash based mac" text.txt
    ```
    Generated Hash:
    ```
    0eecf7180df087de9b3c42cbc0961243
    ```
3. Generate a keyed hash using `HMAC-SHA1` algorithm by the following command
    ```
    openssl dgst -sha1 -hmac "key for hash based mac" text.txt
    ```
    Generated Hash:
    ```
    9935d4ad0a05a67b6bf1e2f57e936a6a00703a72
    ```
4. Generate a keyed hash using `HMAC-SHA256` algorithm by the following command
    ```
    openssl dgst -sha256 -hmac "key for hash based mac" text.txt
    ```
    Generated Hash:
    ```
    85805be3217d735e2c998bca83457f208aa19eb7866b17f4da4bd97eab29ab38
    ```
### Key size in HMAC

- HMAC does not require a key with a fixed size. It can accept keys of any length.
- The key size should be chosen based on the security requirements of the application and the cryptographic algorithm being used.
- However, for HMAC, it's `recommended to use keys that are at least as long as the block size` of the underlying hash function. Such as 16 bytes for HMAC-MD5, 20 bytes for HMAC-SHA1, 32 bytes for HMAC-SHA256.

- If the provided key is shorter than the block size of the hash function, it is usually padded to match the block size using appropriate padding schemes
- Using longer keys can provide better security against brute-force attacks, but excessively long keys may not necessarily enhance security significantly and can incur additional overhead in terms of processing and storage.
