nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end=" ... \n")
print(nome, idade, sep="#", end=" ...\n")
print(nome, idade, sep="#")


numero_1 = input("Informe o primeiro numero para soma: ")
numero_2 = input("Informe o segundo numero para soma: ")


numero_1 = int(numero_1)
numero_2 = int(numero_2)

print(numero_1 + numero_2)

print((int(numero_1)) + (int(numero_2)))
