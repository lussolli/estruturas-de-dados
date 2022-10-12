import numpy

def shell_sort(vetor):
    intervalo = len(vetor)

    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            troca = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > troca:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = troca
        intervalo //= 2

    return vetor

print(shell_sort(numpy.array([15, 88, 12, 26, 14, 3])))
print(shell_sort(numpy.array([9, 8, 7, 6, 5, 4, 3, 2, 1])))
