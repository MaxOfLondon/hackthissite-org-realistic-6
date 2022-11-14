#!/usr/bin/env python3
offset = 762
with open('cipher.txt', 'r') as f:
    cipher_text = f.readline()

num_list = [int(i) for i in cipher_text.split('.') if i]
char_codes_shifted = [a+b+c for (a,b,c) in [num_list[i:i+3] for i in range(0, len(num_list), 3)]]

for i in range(len(char_codes_shifted)):
    print(chr(char_codes_shifted[i] - offset), end='')
print()