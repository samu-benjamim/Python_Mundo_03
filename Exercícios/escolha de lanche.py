from random import randint
print("Escolhedor aleatório de lanches para pedir")
list = []
quant = int(input("Quantas opções você quer inserir?"))
for i in range(0, quant):
    op_1 = str(input(f"Digite a {i+1}º opção:"))
    list.append(op_1)
indice_escolhido = randint(0, quant-1) 
escolha = list[indice_escolhido] 
print(f"A escolha foi {escolha}")