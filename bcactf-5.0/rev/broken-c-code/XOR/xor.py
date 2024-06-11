def xor_decrypt(encrypted_flag, key):
    key_length = len(key)
    decrypted_bytes = []
    
    for i in range(len(encrypted_flag)):
        decrypted_byte = encrypted_flag[i] ^ ord(key[i % key_length])
        decrypted_bytes.append(decrypted_byte)
    
    decrypted_flag = ''.join(chr(byte) for byte in decrypted_bytes)
    return decrypted_flag

# Encrypted flag provided in the challenge
encrypted_flag_hex = "21 0F 0A 15 3F 29 29 6B 13 1C 2C 74 7D 30 5E 50 6E 29 2B 24 19 0C 67 7D 05 54 7C 34 5C 13 32 42 29 62 7B 0F 4E"

# Convert the hexadecimal encrypted flag to bytes
encrypted_flag_bytes = bytes(int(x, 16) for x in encrypted_flag_hex.split())

# Key used for XOR encryption
key = "ClkvKOR8JQA1JB731LeGkU7J4d2khDvrOPI63mM7"

# Decrypt the flag
decrypted_flag = xor_decrypt(encrypted_flag_bytes, key)
print("Decrypted flag:", decrypted_flag)
