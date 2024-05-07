# Task - 4 : Padding

To study the padding scheme let's select the `AES` as the block cipher. The block size of `AES-128` is **128 bit** or **16 Bytes**. Steps for testing with this algorithm are following:

1. Create a text file that has a size which is not multiple of 16 (block size of AES-128) so that padding may be required. The size can be checked using `HEX Workshop`.

2. Now Encrypt using the following commands.

- `ECB mode`
    Encrypt
    ```
    openssl enc -aes-128-ecb -e  -in plain.txt -out encrypted-ecb.bin -K 00112233445566778889aabbccd3322a
    ```
- `CBC mode`
    Encrypt
    ```
    openssl enc -aes-128-cbc -e  -in plain.txt -out encrypted-cbc.bin -K 00112233445566778889aabbccd3322a -iv 01020304050607083241231213124f23
    ```
- `CFB mode`
    Encrypt
    ```
    openssl enc -aes-128-cfb -e  -in plain.txt -out encrypted-cfb.bin -K 00112233445566778889aabbccd3322a -iv 01020304050607083241231213124f23
    ```
- `OFB mode`
    Encrypt
    ```
    openssl enc -aes-128-ofb -e  -in plain.txt -out encrypted-ofb.bin -K 00112233445566778889aabbccd3322a -iv 01020304050607083241231213124f23
    ```

### Observation

```
ECB and CBC modes often need padding, while CFB and OFB modes do not.
```

Here the plain text size was 22 bytes. And `CFB` and `OFB` encrypted files are also 22 bytes. Which means no padding is needed for these algorithms

But however, `ECB` and `CBC` algorithm made the size of encrypted file 32 Bytes which is a multiple of 16 (Block size of AES-128). So here padding is needed incase of these 2 algorithms.

- **ECB (Electronic Codebook):** Requires padding because it operates on fixed-size blocks of data.
- **CBC (Cipher Block Chaining):** Typically requires padding as each block depends on the previous ciphertext block.
- **CFB (Cipher Feedback):** Does not require padding as it operates in a streaming fashion.

- **OFB (Output Feedback):** Also does not require padding as it operates in a streaming fashion.

In summary, ECB and CBC modes often need padding, while CFB and OFB modes do not. Padding ensures that the plaintext length meets the requirements of the encryption mode.
