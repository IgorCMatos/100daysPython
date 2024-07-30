import random

print("Bem-vindo ao Pedra,Papel ou Tesoura.")
user = input("Digite o numero do valor que irar jogar.\n1 - Pedra 2 - Papel 3 - Tesoura\n")
if user not in ('1', '2', '3'):
    print("Valor invalido.")
else:
    user = int(user)
    computer = random.randint(1, 3)
    print("Escolha do computador:", computer)
    if user == computer:
        print("empate")
    elif user == 1 and computer == 3:
        print("Voce ganhou")
    elif user == 3 and computer == 1:
        print("Voce perdeu")
    elif user < computer:
        print("voce perdeu")
    else:
        print("Voce ganhou")