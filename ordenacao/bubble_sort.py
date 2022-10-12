import numpy

def bubble_sort(vetor):
    quantidade_elementos = len(vetor)

    for i in range(quantidade_elementos):
        for j in range(0, quantidade_elementos - i - 1):
            if vetor[j] > vetor[j + 1]:
                troca = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = troca
    
    return vetor

print(bubble_sort(numpy.array([15, 34, 8, 3])))
print(bubble_sort(numpy.array([9, 8, 7, 6, 5, 4, 3, 2, 1])))
