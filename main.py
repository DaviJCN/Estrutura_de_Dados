from ListasEncadeadas.listaEncadeada import ListaSimples
from ListasOrdenadas.listaOrdenada import ListaOrdenada
from Fila.Fila import Fila
from Pilha.Pilha import Pilha
from collections import deque


def main():
    print("-=-"*20)
    print("Lista Simples")
    print("-=-"*20)
    lista = ListaSimples()
    print("Inserindo elementos na lista:")
    lista.insere_inicio(10)
    lista.insere_fim(20)
    lista.insere_inicio(5)
    lista.imprime_lista()
    
    print("Removendo elemento do início:", lista.remove_inicio())
    lista.imprime_lista()
    
    resultado_busca = lista.busca(20)
    print("Resultado da busca pelo elemento 20:", resultado_busca)
    
    print("-=-"*20)
    print("Lista Ordenada")
    print("-=-"*20)
    lista_ord = ListaOrdenada()
    for valor in [50, 20, 40, 10, 30]:
        lista_ord.insere_ordenado(valor)
    lista_ord.imprime_lista()

    print("-=-"*20)
    print("Fila")
    print("-=-"*20)
    fila = Fila()
    print("Enfileirando elementos:")
    fila.enfileirar('A')
    fila.enfileirar('B')
    fila.enfileirar('C')
    fila.imprime_fila()

    print("Desenfileirando elemento:", fila.desenfileirar())
    fila.imprime_fila()

    print("Espiando a frente da fila:", fila.espiar())
    print("Tamanho da fila:", fila.tamanho())

    print("-=-"*20)
    print("Pilha")
    print("-=-"*20)
    pilha = Pilha()
    print("Empilhando elementos:")
    pilha.empilhar(100)
    pilha.empilhar(200)
    pilha.empilhar(300)
    pilha.imprime_pilha()

    print("Desempilhando elemento:", pilha.desempilhar())
    pilha.imprime_pilha()

    print("Espiando o topo da pilha:", pilha.espiar())
    print("Tamanho da pilha:", pilha.tamanho())

main()