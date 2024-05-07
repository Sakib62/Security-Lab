# Task - 2 : Encryption mode - ECB vs CBC

### AES ECB 

1. Download a .bmp file and name it. I named my file [penguin.bmp](penguin.bmp)
2. Encrypt the image with ECB mode, using following command:

    ```
    openssl enc -aes-128-ecb -e -in penguin.bmp -out encryptedECB.bmp -K 00112233445566778889aabbccddeeff
    ```
3. For the .bmp file, the first 54 bytes contain the header information about the picture. But due to encryption, those 54 bytes changed. So, we have to replace the header of encrypted image with that of original image.

4. To do that, open the original image in `HEX Workshop`. Copy the first 54 bytes.

5. Now Open the encrypted image in `HEX Workshop`. Replace the first 54 bytes with the original image's header information.

6. Now open the [encryptedECB.bmp](encryptedECB.bmp) with a picture viewing software to display it. Here, the shape of penguin can be understood, but penguin is not visible completely.

### AES CBC

1. Encrypt the image with CBC mode using following command :

    ```
    openssl enc -aes-128-cbc -e -in penguin.bmp -out encryptedCBC.bmp -K 00112233445566778889aabbccddeeff -iv 20304050607082143234324324233333
    ```
2. Open the original image with `HEX Workshop` and copy the first 54 bytes. These are header information.
3. Open the encrypted image with `HEX Workshop` and replace the first 54 bytes with the original header information.
4. Open the [encryptedCBC.bmp](encryptedCBC.bmp) in any picture viewing software to display it. The image is not recognizable and shape of the penguin cannot be understood.

### My Observation

1. **ECB mode (Electronic Codebook):**

    - Each block of plaintext is encrypted independently with the same key.
    - Identical blocks of plaintext results in identical blocks of ciphertext.
    - Less secure for image encryption as patterns, shape may be recognized from encrypted file.

2. **CBC mode (Cipher Block Chaining):**

    - Each block of plaintext is XORed with the previous ciphertext block before encryption.
    - More resistant to patterns and repetition in the plaintext due to added diffusion.
    - IV (Initialization Vector) is needed for the first block to start the chaining process. Hence, CBC is slower and more complex than ECB mode.

So, conclusion is `CBC is better than ECB for image encryption` as CBC is more resistant to pattern preservation and provides better security.


