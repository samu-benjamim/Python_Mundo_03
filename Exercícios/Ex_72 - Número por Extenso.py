números = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "desesseis", "desessete", "desoito", "desenove", "vinte")
cont = "S"
while cont == "S":    
    while True:
        número = int(input("Digite um numero entre 0 e 20: "))
        if 0 <= número <= 20:
            break
        print("Tente novamente. ", end = "")
    print(f"Você digitou o número {números[número]}")
    cont = str(input("Você deseja continuar? [S/N]")).upper().strip()
print("Obrigado até a próxima!")