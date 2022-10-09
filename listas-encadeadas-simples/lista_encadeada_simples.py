class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeadaSimples:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo
    
    def excluir_inicio(self):
        if self.primeiro == None:
            print("A lista está vazia.")
            return None
        
        temporario = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temporario

    def pesquisa(self, valor):
        if self.primeiro == None:
            print("A lista está vazia.")
            return

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
        return atual

    def excluir_posicao(self, valor):
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        
        return atual
