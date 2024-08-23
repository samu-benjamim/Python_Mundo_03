tupla_primaria = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Difite mais um número: ")), int(input("Digite o último número: ")))
print(f"Voce difitou os valores {tupla_primaria}")
print(f"O valor 9 apareceu {tupla_primaria.count(9)} vezes")
if 3 in tupla_primaria:
    print(f"O valor 3 apareceu na {tupla_primaria.index(3)+1}º posição")
else:
    print("O valor 3 não foi digitado.")
print(f"Os valores pares digitados foram: ", end ="")
for i in tupla_primaria:
    if i % 2 == 0:
        print( i , end = " ")