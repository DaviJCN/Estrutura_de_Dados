from collections import deque

class Fila:
    """
    Implementação de uma fila (queue) utilizando a classe deque do módulo collections.
    """
    def __init__(self):
        self._itens = deque()

    def esta_vazia(self) -> bool:
        """Verifica se a fila está vazia."""
        return not self._itens

    def enfileirar(self, item: any) -> None:
        """Adiciona um item ao final da fila."""
        self._itens.append(item)

    def desenfileirar(self) -> any:
        """Remove e retorna o item da frente da fila."""
        if self.esta_vazia():
            raise IndexError("Fila vazia!")
        return self._itens.popleft()

    def espiar(self) -> any:
        """Retorna o item da frente da fila sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("Fila vazia!")
        return self._itens[0]

    def tamanho(self) -> int:
        """Retorna o número de itens na fila."""
        return len(self._itens)

    def imprime_fila(self) -> None:
        """Imprime os itens da fila da frente para o final."""
        print("Frente -> " + " -> ".join(map(str, self._itens)) + " -> Trás")