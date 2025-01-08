# Instructions:
# -Create an encrypt function which takes two parameters : message and shift number. 
# Then inside this function shift each letter of the message forwards in the alphabet by 
# the shift number and return encrypted text.
# Example Input: Do not stop in your storm!
# Shift number = 4
# Example Output :HS RSX WXST MR CSYV WXSVQ!

# -Create an decrypt function which takes two parameters : message and shift number.
# Then inside this function shift each letter of the message backwards in the alphabet 
# by the shift number and return decrypted text.
# Example Input: HS RSX WXST MR CSYV WXSVQ!
# Shift number = 4
# Example Output: DO NOT STOP IN YOUR STORM!

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(message, shift_number):
    encrypted = ''
    for letter in message:
        if letter.upper() not in alphabet:
            encrypted = encrypted+letter
        else:
            pos = alphabet.index(letter.upper())
            if pos+shift_number > len(alphabet):
                difference = pos+shift_number - len(alphabet)
                encrypted = encrypted+alphabet[difference]
            else:
                encrypted = encrypted+alphabet[pos+shift_number]
    return encrypted

def decrypt(message, shift_number):
    decrypted = ''
    for letter in message:
        if letter.upper() not in alphabet:
            decrypted = decrypted+letter
        else:
            pos = alphabet.index(letter.upper())
            decrypted = decrypted+alphabet[pos-shift_number]
    return decrypted

print(encrypt("Do not stop in your storm!",4))
print(decrypt("HS RSX WXST MR CSYV WXSVQ!",4))
