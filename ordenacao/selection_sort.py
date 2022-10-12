import numpy

def selection_sort(vetor):
    tamanho = len(vetor)

    for i in range(tamanho):
        indice_minimo = i
        for j in range(i + 1, tamanho):
            if vetor[indice_minimo] > vetor[j]:
                indice_minimo = j

        troca = vetor[i]
        vetor[i] = vetor[indice_minimo]
        vetor[indice_minimo] = troca

    return vetor

print(selection_sort(numpy.array([15, 34, 8, 3])))
print(selection_sort(numpy.array([9, 8, 7, 6, 5, 4, 3, 2, 1])))
