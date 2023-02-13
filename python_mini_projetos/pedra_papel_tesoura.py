import random 

usuario_venceu = 0
computador_venceu = 0
empate = 0

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogada_usuario = input("Digite pedra/papel/tesoura ou Q para sair: ").lower()

    if jogada_usuario == "q":
        break


    if jogada_usuario not in opcoes:
        continue

    numero_aleatorio = random.randint(0, 2)
    # pedra = 0, papel = 1, tesoura = 2
    jogada_computador = opcoes[numero_aleatorio]
    print(f"O computador escolheu {jogada_computador}.")

    if jogada_usuario == "pedra" and jogada_computador == "tesoura":
        print("Você venceu!")
        usuario_venceu += 1

    elif jogada_usuario == "papel" and jogada_computador == "pedra":
        print("Você venceu!")
        usuario_venceu += 1

    elif jogada_usuario == "tesoura" and jogada_computador == "papel":
        print("Você venceu!")
        usuario_venceu += 1

    elif jogada_usuario == "pedra" and jogada_computador == "pedra":
        print("Empatou!")
        empate += 1

    elif jogada_usuario == "papel" and jogada_computador == "papel":
        print("Empatou!")
        empate += 1
    
    elif jogada_usuario == "tesoura" and jogada_computador == "tesoura":
        print("Empatou!")
        empate += 1

    else:
        print("Você perdeu!")
        computador_venceu += 1
    
print(f"Você venceu {usuario_venceu} vezes")
print(f"O computador venceu {computador_venceu} vezes")
print(f"O jogo empatou {empate} vezes")
print("Tchau! Obrigado por jogar!")