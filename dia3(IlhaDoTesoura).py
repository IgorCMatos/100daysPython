
print("Bem-vindo à ilha do tesouro")
first = input("Você encontra uma bifurcação. Deseja ir para 'esquerda' ou 'direita'? ").lower().strip()
if first == 'esquerda':
    second = input("Você chega numa praia. Você irá 'nadar' ou 'esperar'? ").lower().strip()
    if second == 'esperar':
        third = input("Você continua andando na praia e encontra uma caverna com 3 portas.\nPara qual você irá? 'Vermelha', 'Amarelo' ou 'Azul'. ").lower().strip()
        if third == 'amarelo':
            print("Você ganhou!!!!")
        elif third == 'vermelha':
            print("Fim de Jogo, Você foi pego numa armadilha.")
        elif third == 'azul':
            print("Fim de Jogo, Você caiu num buraco.")
        else:
            print("Tecla inválida, Fim de jogo.")
    elif second == 'nadar':
        print("Fim de Jogo, Você foi devorado por um Tubarão.")
    else:
        print("Tecla inválida, Fim de jogo.")
elif first == 'direita':
    print("Fim de Jogo, Você caiu numa areia movediça.")
else:
    print("Tecla inválida, Fim de jogo.")
