from random import randint
number = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os valores sorteados foram: ", end="")
for i in number:
    print(f"{i} ", end="")
number_ordem = sorted(number)
print(f"\nO menor foi {number_ordem[0]}")
print(f"O maior foi {number_ordem[-1]}")