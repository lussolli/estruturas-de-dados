from pilha import Pilha

pilha = Pilha(5)
pilha.desempilhar()
pilha.empilhar(10)
pilha.empilhar(20)
print(pilha.ver_topo())
pilha.desempilhar()
print(pilha.ver_topo())
