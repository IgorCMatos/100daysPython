import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao PyPassword Generator!")
nr_letters= int(input("Quantas letras você gostaria em sua senha?\n")) 
nr_symbols = int(input(f"Quantos símbolos você gostaria?\n"))
nr_numbers = int(input(f"Quantos números você gostaria?\n"))

password_list = []
while nr_letters > 0:
    password_list += random.choice(letters)
    nr_letters -= 1

while nr_symbols > 0:
    password_list += random.choice(symbols)
    nr_symbols -= 1

while nr_numbers > 0:
    password_list += random.choice(numbers)
    nr_numbers -= 1

random.shuffle(password_list)
password = ''.join(password_list)

print(f"Sua senha é: {password}")
