# Task - 7 : Keyed hash and HMAC

The instructions are followed in the following steps:

1. Create a text file and add some text. I named it [text.txt](text.txt). Now copy the text inside and paste into a new text file named [for-md5.txt](for-md5.txt).
2. Generate the hash value H1 for this file using `MD5` hash algorithm using the following command:
    ```
    openssl dgst -md5 -hmac "this is task 7" for-md5.txt
    ```
    Generated Hash, H1:
    ```
    482c48d5234eff1ca0a1cb3f6d47f8fc
    ```
3. Open the file using `HEX Workshop` and change one bit (any bit) of the file. HEX workshop is used to edit binary files.
4. Again generate the hash value H2 for this modified file.
    ```
    openssl dgst -md5 -hmac "this is task 7" for-md5.txt
    ```
    Generated Hash, H2:
    ```
    823a13f73f84674bd64ec678e074ef16
    ```
5. Hash value, H1 and H2 are not same. Following code is used to calculate how many bits are same between them.
    ```py
    def checkSame(h1, h2):
        i = 0
        cnt = 0
        for ch in h1:
            if ch==h2[i]:
                cnt = cnt + 1
            i = i + 1
        
        print("Number of same bit: ", cnt)

    h1 = "482c48d5234eff1ca0a1cb3f6d47f8fc"
    h2 = "823a13f73f84674bd64ec678e074ef16"

    checkSame(h1, h2)
    ```

    Output:
    ```
    Number of same bit : 1
    ```
    Changing only one bit has changed the hash value. Only one bit is same as before in the hash value.

<br>

Now let's repeat the instructions for `SHA-256` algorithm.

Copy the text of [text.txt](text.txt) and paste into a new file named [for-sha256.txt](for-sha256.txt)

- Generate the hash value, H1 for this file using `SHA-256` algorithm using the following command:
    ```
    openssl dgst -sha256 -hmac "this is task 7" for-sha256.txt
    ```
    Generated Hash, H1:
    ```
    3f99d45079d1ad2dd1310ffc66f6bc92e6c119cde8cf093b5dadbcb62b1a1945
    ```
- After changing a bit in the file, Generated Hash, H2:
    ```
    45837b84493aefc8b6ae765ecc39112563f221de67a2d372efed28a5b6c87e50
    ```
- Run the [count.py](count.py) with the hash value H1 and H2.
    ```
    Number of same bit : 2
    ```
So, any single modification in the source file will change hash value to a great extent.

This property of hash functions is widely used in various applications for data integrity verification, digital signatures, and detecting unauthorized modifications.
