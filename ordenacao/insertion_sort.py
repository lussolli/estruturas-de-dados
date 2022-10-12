import numpy

def insertion_sort(vetor):
    tamanho = len(vetor)

    for i in range(1, tamanho):
        marcado = vetor[i]

        j = i - 1
        while j >= 0 and marcado < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = marcado

    return vetor

print(insertion_sort(numpy.array([15, 34, 8, 3])))
print(insertion_sort(numpy.array([9, 8, 7, 6, 5, 4, 3, 2, 1])))
