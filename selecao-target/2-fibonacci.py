### FIBONACCI
n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1
contains = [0, 1, 1]

if (n == 1) or (n == 2):
    print("1")
else:
    count = 3
    while count <= n:
        termo = ultimo + penultimo
        contains.append(termo)
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)

if n in contains:
    print(f'A entrada {n} pertence a sequência.')
else:
    print(f'A entrada {n} não pertence a sequência.')
