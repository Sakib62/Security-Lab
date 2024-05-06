def decrypt_caesar_cipher(cipher_text):
    for shift in range(26):
        plain_text = ""
        for char in cipher_text:
            if char.isalpha():
                shifted = ord(char) - shift
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                plain_text += chr(shifted)
            else:
                plain_text += char
        print('Shift #%s: %s' % (shift, plain_text))

message = 'odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo'

decrypt_caesar_cipher(message)