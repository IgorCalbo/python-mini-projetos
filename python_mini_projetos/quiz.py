print("Seja bem-vindo ao quiz!")

jogando = input("Você gostaria de jogar? ")

if jogando.lower() != "sim":
    quit()

print("Ok, Vamos jogar :) ")
pontos = 0

resposta = int(input("Quantas vezes o Brasil foi campeão mundial de futebol? "))
if resposta == 5:
    print("Correto!")
    pontos += 1
else:
    print("Incorreto!")

resposta = int(input("Em que ano foi proclamada a independência do Brasil? "))
if resposta == 1822:
    print("Correto!")
    pontos += 1
else:
    print("Incorreto!")

resposta = input("Quem foi o inventor do avião? ")
if resposta.lower() == "santos dumont":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto!")

resposta = input("Qual livro brasileiro mais traduzido no mundo? ")
if resposta.lower() == "o alquimista":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto!")

# print(f"You got {pontos} questions correct!")
print("Você acertou " +  str(pontos) + " de 4 questões, obrigado por jogar.")
print("A porcentagem foi de " + str((pontos / 4) * 100) + "%!")
