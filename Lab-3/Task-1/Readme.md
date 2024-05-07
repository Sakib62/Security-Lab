# Task - 1 : AES encryption using different modes

The modes that will be used are : AES-128-CBC, AES-128-CFB, AES-128-ECB

The steps followed are :

1. Create a text file and add some texts.
2. `Encrypt` this file with `AES-128-CBC` using following command:
    
    ```
    $ openssl enc -aes-128-cbc -e -in test.txt -out encrypt-aes-128-cbc.bin -k 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060708
    ```
    Encrypted File : [encrypt-aes-128-cbc.bin](encrypt-aes-128-cbc.bin)

3. `Decrypt` the encrypted file with `AES-128-CBC` using following command:

    ```
    openssl enc -aes-128-cbc -d -in encrypt-aes-128-cbc.bin -out decrypt-aes-128-cbc.txt -k 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060708
    ```
    Decrypted File : [decrypt-aes-128-cbc.txt](decrypt-aes-128-cbc.txt)

Similarly, we will encrypt and decrypt the file using two other modes.

### AES-128-CFB

- Encryption

    ```
    openssl enc -aes-128-cfb -e -in test.txt -out encrypt-aes-128-cfb.bin -k 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060708
    ```
    Encrypted File : [encrypt-aes-128-cfb.bin](encrypt-aes-128-cfb.bin)

- Decryption

    ```
    openssl enc -aes-128-cfb -d -in encrypt-aes-128-cfb.bin -out decrypt-aes-128-cfb.txt -k 00112233445566778889aabbccddeeff -iv 01020304050607080102030405060708
    ```
    Decrypted File : [decrypt-aes-128-cfb.txt](decrypt-aes-128-cfb.txt)

### AES-128-ECB

In ECB mode, no iv (initialisation vector is needed)

- Encryption

    ```
    openssl enc -aes-128-ecb -e -in test.txt -out encrypt-aes-128-ecb.bin -k 00112233445566778889aabbccddeeff
    ```
    Encrypted File : [encrypt-aes-128-ecb.bin](encrypt-aes-128-ecb.bin)

- Decryption

    ```
    openssl enc -aes-128-ecb -d -in encrypt-aes-128-ecb.bin -out decrypt-aes-128-ecb.txt -k 00112233445566778889aabbccddeeff
    ```
    Decrypted File : [decrypt-aes-128-ecb.txt](decrypt-aes-128-ecb.txt)
