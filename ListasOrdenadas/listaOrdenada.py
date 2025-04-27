class ListaOrdenada:
    """
    Implementação de uma lista ordenada (em ordem crescente).
    Assume que os itens são comparáveis (por exemplo, números).
    """
    class Node:
        def __init__(self, item: any):
            self.item = item
            self.next = None

        def __repr__(self):
            return f"Node({self.item})"

    def __init__(self):
        self.head = None

    def insere_ordenado(self, item: any) -> None:
        """Insere um item na lista mantendo a ordem crescente."""
        novo = ListaOrdenada.Node(item)
        if self.head is None or item < self.head.item:
            novo.next = self.head
            self.head = novo
        else:
            atual = self.head
            while atual.next is not None and atual.next.item < item:
                atual = atual.next
            novo.next = atual.next
            atual.next = novo

    def imprime_lista(self) -> None:
        """Imprime os itens da lista ordenada."""
        atual = self.head
        elementos = []
        while atual:
            elementos.append(str(atual.item))
            atual = atual.next
        print(" -> ".join(elementos) + " -> None")