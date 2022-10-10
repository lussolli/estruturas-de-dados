def soma(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

print(soma(10))

def soma_recursiva(n):
    if n == 0:
        return 0
    
    return n + soma_recursiva(n - 1)

print(soma(10))
