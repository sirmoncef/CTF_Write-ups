def check_flag(producer_value):
    k = [0x46, 0x2d, 0x62, 0x11, 0x6b, 0x4c, 0x72, 0x5f, 0x76, 0x38, 0x19, 0x28, 0x5f, 0x31, 0x36, 0x63, 0xf7, 0xb1, 0x69, 0x2a, 0x18, 0x5e, 0x36, 0x1, 0x37, 0x3a, 0x1c, 0x5, 0x11, 0x56, 0xe5, 0x7b, 0x64, 0x2c, 0x11, 0x14, 0x53, 0x5a, 0x35, 0x17, 0x41, 0x62, 0x3]
    flag_length = len(k)
    flag = ''
    char_codes = []

    for i in range(flag_length):
        char_code = k[i] ^ (producer_value % (0x75 + i))
        char_codes.append(char_code)
        if char_code < 32 or char_code > 126:  # printable ASCII range
            return None
        flag += chr(char_code)

    print(f'Intermediate char codes for producer_value {producer_value}: {char_codes}')
    return flag

# Using the provided producer_value
producer_value = 283548893274
flag = check_flag(producer_value)
if flag:
    print(f'Possible flag: {flag}, with producer_value: {producer_value}')
else:
    print(f'No valid flag produced with producer_value: {producer_value}')
