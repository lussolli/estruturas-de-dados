import numpy

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = numpy.empty(self.capacidade, dtype=int)
    
    # O(n)
    def imprimir(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio.")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, "-", self.valores[i])

    # O(1) - O(2)
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima já atingida.")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
    
    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        
        return -1
    
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)

        if posicao == -1:
            return -1
        
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]
        
        self.ultima_posicao -= 1
