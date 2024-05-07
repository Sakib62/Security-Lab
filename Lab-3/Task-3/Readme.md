# Task - 3 : Encryption mode – corrupted cipher text

The goal of this task is to understand the properties of various encryption modes.

1. Create a text file that is at least 64 bytes long.
2. Encrypt the file using AES-128 Cipher using the following command
    ```
    openssl enc -aes-128-ecb -e -in plaintext.txt -out encrypted-ecb.bin -K 00112233445566778889aabbccddeeff
    ```
3. Corrupt a single bit of the 30th byte in the encrypted file. Open the file in `HEX Workshop` and change the first bit of 30th byte. [Editing encrypted file](edit-encrypted.png) : goto 30th byte from the beginning of the encrypted file, cursor will be next to the byte. Here 30th byte was 85 in hexadecimal. So, modified it to 86. Thus corrupting the first bit of 30th byte.

4. Decrypt the file using following command
    ```
    openssl enc -aes-128-ecb -d -in encrypted-ecb.bin -out decrypted-ecb.txt -K 00112233445566778889aabbccddeeff
    ```

Let's repeat these steps for other modes:

1. `CBC mode`
    Encrypt
    
    ```
    openssl enc -aes-128-cbc -e -in plaintext.txt -out encrypted-cbc.bin -K 00112233445566778889aabbccddeeff -iv 20304050607082143234324324233333
    ```

    Decrypt the corrupted encrypted file

    ```
    openssl enc -aes-128-cbc -d -in encrypted-cbc.bin -out decrypted-cbc.txt -K 00112233445566778889aabbccddeeff -iv 20304050607082143234324324233333
    ```
2. `CFB mode`
    Encrypt
    ```
    openssl enc -aes-128-cfb -e -in plaintext.txt -out encrypted-cfb.bin -K 00112233445566778889aabbccddeeff -iv 20304050607082143234324324233333
    ```

    Decrypt the corrupted encrypted file

    ```
    openssl enc -aes-128-cfb -d -in encrypted-cfb.bin -out decrypted-cfb.txt -K 00112233445566778889aabbccddeeff -iv 20304050607082143234324324233333
    ```

3. `OFB mode`
    Encrypt
    ```
    openssl enc -aes-128-ofb -e -in plaintext.txt -out encrypted-ofb.bin -K 00112233445566778889aabbccddeeff -iv 20304050607082143234324324233333
    ```

    Decrypt the corrupted encrypted file

    ```
    openssl enc -aes-128-ofb -d -in encrypted-ofb.bin -out decrypted-ofb.txt -K 00112233445566778889aabbccddeeff -iv 20304050607082143234324324233333
    ```
### Observation

Original File

```
So this is it! This is the end! Part of the journey is the end. Don't cry because it's over. Smile because it happened.
```

| Mode |       Corrupted File        |
|------|----------------------------|
| ECB  |So this is it! T�3R35�/��%\�مPart of the journey is the end. Don't cry because it's over. Smile because it happened.|
| CBC  |So this is it! T�Z�U��$i\|>O`��Part of the jlurney is the end. Don't cry because it's over. Smile because it happened.|
| CFB  |So this is it! This is the ene! ����m�%�\��3��ney is the end. Don't cry because it's over. Smile because it happened.|
| OFB  |So this is it! This is the enc! Part of the journey is the end. Don't cry because it's over. Smile because it happened.|


### Analysis

Based on the provided results, let's analyze the information recovery for each encryption mode:

1. **ECB (Electronic Codebook):**

    - Recoverable Information: "So this is it! T" (16 bytes)
    - Explanation: In ECB mode, each block is encrypted independently. Therefore, the corruption only affects the specific block where it occurred. The rest of the plaintext remains intact.

2. **CBC (Cipher Block Chaining):**

    - Recoverable Information: "So this is it! T" (16 bytes)
    - Explanation: While CBC mode encrypts blocks in a chained manner, the corruption in one block affects the decryption of subsequent blocks. However, the first block can still be recovered as it only depends on the IV and the first block of ciphertext.

3. **CFB (Cipher Feedback):**

    - Recoverable Information: "So this is it! This is the en" (32 bytes)
    - Explanation: In CFB mode, the corruption in one ciphertext block affects the decryption of subsequent blocks. However, due to the feedback mechanism, only a part of the subsequent blocks is corrupted. As a result, more information can be recovered compared to CBC mode.

4. **OFB (Output Feedback):**

    - Recoverable Information: "So this is it! This is the en" (32 bytes)
    - Explanation: Similar to CFB mode, the corruption in one ciphertext block affects the decryption of subsequent blocks. However, in OFB mode, the feedback mechanism is independent of the plaintext, resulting in a similar recovery as in CFB mode.

**Summary:**

- ECB mode offers the least security and diffusion, as evident from the limited recoverable information.
- CBC mode provides better security compared to ECB but still suffers from partial corruption propagation.

- CFB and OFB modes offer improved diffusion, allowing for more recoverable information compared to CBC mode, although they are still susceptible to partial corruption propagation.

