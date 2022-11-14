#!/usr/bin/env python3

cipher_text = '.296.294.255.268.313.278.311.270.290.305.322.252.276.286.301.305.264.301.251.269.274.311.304.230'
num_list = [int(i) for i in cipher_text.split('.') if i]
char_codes_shifted = [a+b+c for (a,b,c) in [num_list[i:i+3] for i in range(0, len(num_list), 3)]]

for i in range(718, 845 +1):
    print(i, end=":")
    for j in range(0,8):
        print(chr(char_codes_shifted[j] - i), end='') if (char_codes_shifted[j] -i) >= ord(' ') else ' '
    print()
