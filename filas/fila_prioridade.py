import numpy

class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = numpy.empty(self.capacidade, dtype=int)
    
    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A fila está cheia.")
            return
        
        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            auxiliar = self.numero_elementos - 1
            while auxiliar >= 0:
                if valor > self.valores[auxiliar]:
                    self.valores[auxiliar + 1] = self.valores[auxiliar]
                else:
                    break
                auxiliar -= 1
            self.valores[auxiliar + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila está vazia.")
            return
        
        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos - 1]

fila = FilaPrioridade(5)
print(fila.primeiro())
fila.enfileirar(30)
print(fila.primeiro())
fila.enfileirar(50)
print(fila.primeiro())
fila.enfileirar(10)
print(fila.primeiro())
fila.enfileirar(40)
fila.enfileirar(20)
print("Valores:", fila.valores)
fila.desenfileirar()
print(fila.primeiro())
