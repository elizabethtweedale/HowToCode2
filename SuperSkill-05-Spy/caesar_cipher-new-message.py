# Caesar Cipher - Python Code - Elizabeth Tweedale

# t is the text string for decoding/encoding
# k is the key integer
# decode is a boolean
def caesar(t, k, decode = False):
	if decode: k = 26 - k   # check if you are decoding or encoding
                                # if decode = True, shift the key forward
                                # to 26 - the key amount
                                # (returning it to its original position)
	return "".join([chr((ord(i) - 65 + k) % 26 + 65)                # the math behind shifting our letters
				for i in t.upper()                      # for every letter in the text
				if ord(i) >= 65 and ord(i) <= 90 ])     # check if the character is a letter between A-Z
                               

# Test the code:

# Change the text and key to test different messages
text = "sending help meet in paris at the meeting point in three days at noon"
key = 8

encr = caesar(text, key)
decr = caesar(encr, key, decode = True)

print (text)
print (encr)
print (decr)

# Output:

#     Plain text = The quick brown fox jumped over the lazy dogs
# Encrypted text = AMVLQVOPMTXUMMBQVXIZQAIBBPMUMMBQVOXWQVBQVBPZMMLIGAIBVWWV
# Decrypted text = SENDINGHELPMEETINPARISATTHEMEETINGPOINTINTHREEDAYSATNOON
