import random

def generate_passwords(number, length, chars, use_upper, use_lower, use_digits, use_special):
    passwords = []
    for _ in range(number):
        password = []

        if use_upper:
            password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if use_lower:
            password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        if use_digits:
            password.append(random.choice('0123456789'))
        if use_special:
            password.append(random.choice('!@#$%^&*()-_=+;:,.<>?~`'))

        while len(password) < length:
            password.append(random.choice(chars))
        
        random.shuffle(password)
        passwords.append(''.join(password))
        
    return passwords

def get_positive_integer(prompt):
    value = input(prompt)
    while not value.isdigit() or int(value) <= 0:
        print('Please enter a valid positive number.')
        value = input(prompt)
    return int(value)

def get_filename(prompt):
    while True:
        filename = input(prompt)
        if filename.endswith('.txt'):
            return filename
        else:
            print("Please enter a file name with the extension '.txt'.")

print('Welcome to your Password Generator')

use_upper = input('Include uppercase letters? (y/n) ').lower() == 'y'
use_lower = input('Include lowercase letters? (y/n) ').lower() == 'y'
use_digits = input('Include numbers? (y/n) ').lower() == 'y'
use_special = input('Include special characters? (y/n) ').lower() == 'y'

chars = ''
if use_upper:
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if use_lower:
    chars += 'abcdefghijklmnopqrstuvwxyz'
if use_digits:
    chars += '0123456789'
if use_special:
    chars += '!@#$%^&*()-_=+;:,.<>?~`'

if not chars:
    print('You must select at least one character type!')
    exit()

number = get_positive_integer('Amount of passwords to generate: ')
length = get_positive_integer('Input your password length: ')

print('\nHere are your passwords: ')
for pwd in generate_passwords(number, length, chars, use_upper, use_lower, use_digits, use_special):
    print(pwd)

save_to_file = input('Do you want to save the passwords to a file? (y/n) ').lower() == 'y'

if save_to_file:
    filename = get_filename('Enter the filename (e.g., passwords.txt): ')
    with open(filename, 'w') as file:
        for pwd in generate_passwords(number, length, chars, use_upper, use_lower, use_digits, use_special):
            file.write(pwd + '\n')
    print(f'Passwords saved to {filename}')