def encryptCaesarCipher(text, shift):
    """
    Encrypts a given text using the Caesar cipher with the specified shift.
    
    :param text: The text to be encrypted.
    :param shift: The number of positions to shift each character.
    :return: The encrypted text.
    """
    encryptedText = ""
    
    for char in text:
        if char.isalpha():
            isUpperCase = char.isupper()
            charCode = ord(char)
            shiftedCharCode = charCode + shift
            
            if isUpperCase:
                if shiftedCharCode > ord('Z'):
                    shiftedCharCode -= 26
                elif shiftedCharCode < ord('A'):
                    shiftedCharCode += 26
            else:
                if shiftedCharCode > ord('z'):
                    shiftedCharCode -= 26
                elif shiftedCharCode < ord('a'):
                    shiftedCharCode += 26
                    
            encryptedText += chr(shiftedCharCode)
        else:
            encryptedText += char
    
    return encryptedText


def decryptCaesarCipher(encryptedText, shift):
    """
    Decrypts a Caesar cipher encrypted text with the specified shift.
    
    :param encryptedText: The text to be decrypted.
    :param shift: The number of positions to shift each character.
    :return: The decrypted text.
    """
    return encryptCaesarCipher(encryptedText, -shift)

# Example Usage
if __name__ == "__main__":
    plaintext = "Hello, World! 123"
    shift = 3

    encrypted_text = encryptCaesarCipher(plaintext, shift)
    decrypted_text = decryptCaesarCipher(encrypted_text, shift)

    print("Original Text: ", plaintext)
    print("Encrypted Text: ", encrypted_text)
    print("Decrypted Text: ", decrypted_text)
