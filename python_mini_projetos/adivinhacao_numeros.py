import random 

limite = input("Digite o límite: ")

if limite.isdigit():
    limite = int(limite)

    if limite <= 0:
        print("Por favor, digite um número maior que 0 na próxima vez")
        quit()
else:
    print("Por favor, digite um número na próxima vez")
    quit()

numero_aleatorio = random.randint(0, limite)
palpites = 0

print(f"Tente adivinhar o número entre 0 a {limite}")

while True:
    palpites += 1
    palpite_usuario = input("Qual seu palpite: ")
    if palpite_usuario.isdigit():
        palpite_usuario = int(palpite_usuario)
    else:
        print("Por favor, digite um número na próxima vez")
        continue 

    if palpite_usuario == numero_aleatorio:
        print("Você acertou!")
        break
    elif palpite_usuario > numero_aleatorio:
        print("Seu palpite foi maior que o número")
    else:
        print("Seu palpite foi menor que o número")
    
print(f"Você acertou em {palpites} palpites!")