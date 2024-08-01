def caesar_shift(char, shift):
    if char.isalpha():
        shift = shift % 26
        code = ord(char) + shift
        if char.islower():
            if code > ord('z'):
                code -= 26
            elif code < ord('a'):
                code += 26
        elif char.isupper():
            if code > ord('Z'):
                code -= 26
            elif code < ord('A'):
                code += 26
        return chr(code)
    else:
        return char

def encrypt_string(input_string, shift):
    words = input_string.split()
    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]
    
    encrypted_string = ' '.join(words)
    
    encrypted_chars = [caesar_shift(char, shift) for char in encrypted_string]
    
    return ''.join(encrypted_chars)

input_string = "This is an example of the encryption algorithm"
shift = 3
encrypted = encrypt_string(input_string, shift)
print(encrypted)
