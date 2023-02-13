
def exibe():
    with open("senhas.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            data = linha.rstrip()
            usuario, senha = data.split("|")
            print("Usuario:", usuario, "| Senha:", senha)

def adiciona():
    nome = input("Nome da Conta: ")
    senha = input("Senha: ") 

    with open("senhas.txt", "a") as arquivo:
        arquivo.write(nome + "|" + senha + "\n")

while True:
    opcao = input("Você gostaria de adicionar uma nova senha(adicionar), exibir as senhas existentes(exibir) ou sair(aperte Q): ").lower()
    if opcao == "q":
        break

    if opcao == "exibir":
        exibe()
    elif opcao == "adicionar":
        adiciona()
    else:
        print("Opção Inválida.")
        continue    