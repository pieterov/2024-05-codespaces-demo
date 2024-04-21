def generate_numbers():
    pi_digits = '3141592653'
    
    a = int(pi_digits[0:3])
    b = int(pi_digits[3:5]) - int(pi_digits[0]) + int(pi_digits[2])
    c = int(pi_digits[5:9]) % int(pi_digits[9])
    
    return a, b, c

print(generate_numbers())