from ListasEncadeadas.node import Node

class ListaSimples:
    """
    Implementação de uma lista encadeada simples.
    Possui métodos para inserção (início e fim), remoção, busca e impressão dos elementos.
    """
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def insere_inicio(self, item: any) -> None:
        """Insere um novo nó no início da lista."""
        novo = Node(item)
        novo.next = self.head
        self.head = novo

    def insere_fim(self, item: any) -> None:
        """Insere um novo nó no final da lista."""
        novo = Node(item)
        if self.is_empty():
            self.head = novo
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = novo

    def remove_inicio(self) -> any:
        """Remove o nó do início da lista e retorna seu valor."""
        if self.is_empty():
            raise Exception("Lista vazia!")
        removido = self.head
        self.head = self.head.next
        return removido.item

    def remove_item(self, item: any) -> bool:
        """
        Remove o primeiro nó que contém o valor especificado.
        Retorna True se o item foi removido, False caso contrário.
        """
        atual = self.head
        anterior = None
        while atual:
            if atual.item == item:
                if anterior:
                    anterior.next = atual.next
                else:
                    self.head = atual.next
                return True
            anterior = atual
            atual = atual.next
        return False

    def busca(self, item: any) -> Node:
        """Busca e retorna o nó contendo o item, ou None se não encontrado."""
        atual = self.head
        while atual:
            if atual.item == item:
                return atual
            atual = atual.next
        return None

    def imprime_lista(self) -> None:
        """Imprime os itens da lista."""
        atual = self.head
        elementos = []
        while atual:
            elementos.append(str(atual.item))
            atual = atual.next
        print(" -> ".join(elementos) + " -> None")