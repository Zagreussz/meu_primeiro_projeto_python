senha='projetopython123'

while True:
    tentativa=(input("Digite a senha correta: "))

    if tentativa == senha:
        print("Senha Correta")
        break
    else:
        print("Senha incorreta, tente novamente ")