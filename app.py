import random

def generate_passwords(number, length, chars, use_upper, use_lower, use_digits, use_special):
    """
    Gera uma lista de senhas com base nos parâmetros fornecidos.

    Args:
        number (int): Número de senhas a serem geradas.
        length (int): Comprimento de cada senha.
        chars (str): Conjunto de caracteres a serem usados na geração das senhas.
        use_upper (bool): Incluir letras maiúsculas.
        use_lower (bool): Incluir letras minúsculas.
        use_digits (bool): Incluir dígitos.
        use_special (bool): Incluir caracteres especiais.

    Returns:
        list: Lista de senhas geradas.
    """
    passwords = []
    for _ in range(number):
        password = []

        # Adiciona pelo menos um caractere de cada tipo selecionado
        if use_upper:
            password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if use_lower:
            password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        if use_digits:
            password.append(random.choice('0123456789'))
        if use_special:
            password.append(random.choice('!@#$%^&*()-_=+;:,.<>?~`'))

        # Completa a senha com caracteres aleatórios até atingir o comprimento desejado
        while len(password) < length:
            password.append(random.choice(chars))
        
        # Embaralha os caracteres da senha
        random.shuffle(password)
        passwords.append(''.join(password))
        
    return passwords

def get_positive_integer(prompt):
    """
    Solicita ao usuário um número inteiro positivo.

    Args:
        prompt (str): Mensagem a ser exibida ao solicitar a entrada do usuário.

    Returns:
        int: Número inteiro positivo fornecido pelo usuário.
    """
    value = input(prompt)
    while not value.isdigit() or int(value) <= 0:
        print('Please enter a valid positive number.')
        value = input(prompt)
    return int(value)

def get_filename(prompt):
    """
    Solicita ao usuário um nome de arquivo com a extensão .txt.

    Args:
        prompt (str): Mensagem a ser exibida ao solicitar a entrada do usuário.

    Returns:
        str: Nome do arquivo fornecido pelo usuário.
    """
    while True:
        filename = input(prompt)
        if filename.endswith('.txt'):
            return filename
        else:
            print("Please enter a file name with the extension '.txt'.")

# Mensagem de boas-vindas
print('Welcome to your Password Generator')

# Solicita ao usuário se deseja incluir letras maiúsculas, letras minúsculas, dígitos e caracteres especiais
use_upper = input('Include uppercase letters? (y/n) ').lower() == 'y'
use_lower = input('Include lowercase letters? (y/n) ').lower() == 'y'
use_digits = input('Include numbers? (y/n) ').lower() == 'y'
use_special = input('Include special characters? (y/n) ').lower() == 'y'

# Constrói o conjunto de caracteres com base nas escolhas do usuário
chars = ''
if use_upper:
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if use_lower:
    chars += 'abcdefghijklmnopqrstuvwxyz'
if use_digits:
    chars += '0123456789'
if use_special:
    chars += '!@#$%^&*()-_=+;:,.<>?~`'

# Verifica se pelo menos um tipo de caractere foi selecionado
if not chars:
    print('You must select at least one character type!')
    exit()

# Solicita ao usuário a quantidade de senhas a serem geradas
number = get_positive_integer('Amount of passwords to generate: ')
# Solicita ao usuário o comprimento de cada senha
length = get_positive_integer('Input your password length: ')

# Exibe as senhas geradas
print('\nHere are your passwords: ')
for pwd in generate_passwords(number, length, chars, use_upper, use_lower, use_digits, use_special):
    print(pwd)

# Pergunta ao usuário se deseja salvar as senhas em um arquivo
save_to_file = input('Do you want to save the passwords to a file? (y/n) ').lower() == 'y'

# Verifica se o usuário deseja salvar as senhas em um arquivo
if save_to_file:
    # Solicita ao usuário o nome do arquivo com a extensão .txt
    filename = get_filename('Enter the filename (e.g., passwords.txt): ')
    
    # Abre o arquivo no modo de escrita
    with open(filename, 'w') as file:
        # Gera as senhas e escreve cada uma em uma nova linha no arquivo
        for pwd in generate_passwords(number, length, chars, use_upper, use_lower, use_digits, use_special):
            file.write(pwd + '\n')
    
    # Informa ao usuário que as senhas foram salvas no arquivo especificado
    print(f'Passwords saved to {filename}')