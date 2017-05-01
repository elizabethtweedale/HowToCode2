# The Vigenere Cipher - Python Code - Elizabeth Tweedale

from itertools import starmap, cycle
 
def encrypt(message, key):
 
    # convert to uppercase.
    # strip out non-alpha characters.
    message = filter(str.isalpha, message.upper())
 
    # single letter encrpytion.
    def enc(c,k): return chr(((ord(k) + ord(c) - 2*ord('A')) % 26) + ord('A'))
 
    return "".join(starmap(enc, zip(message, cycle(key))))
 
def decrypt(message, key):
 
    # single letter decryption.
    def dec(c,k): return chr(((ord(c) - ord(k) - 2*ord('A')) % 26) + ord('A'))
 
    return "".join(starmap(dec, zip(message, cycle(key))))


# Test the code:

text = "Hello everyone, I love to code and am training to be a spy!"
key = "VIGENERECIPHER"
 
encr = encrypt(text, key)
decr = decrypt(encr, key)
 
print (text)
print (encr)
print (decr)


# Output:

#     Plain text = Hello everyone, I love to code and am training to be a spy!
# Encrypted text = CMRPBIMITGDUIZGWBIGSTSFMPUHRHBXEVRZRIBDIIRNXE
# Decrypted text = HELLOEVERYONEILOVETOCODEANDAMTRAININGTOBEASPY
