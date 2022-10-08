from lista_encadeada_simples import ListaEncadeadaSimples

lista = ListaEncadeadaSimples()
print(lista.pesquisa(12))
lista.insere_inicio(5)
lista.insere_inicio(6)
lista.insere_inicio(7)
lista.insere_inicio(8)
lista.insere_inicio(9)
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_posicao(6)
lista.excluir_posicao(12)
lista.mostrar()
pesquisa = lista.pesquisa(7)
if pesquisa != None:
    print("Valor encontrado:", pesquisa.valor)
else:
    print("Valor não encontrado.")
