class Pilha:
    """
    Implementação de uma pilha (stack).
    Utiliza uma estrutura interna para manter os itens e a referência ao topo.
    Possui métodos para adicionar (empilhar), remover (desempilhar),
    verificar o topo (espiar) e verificar se a pilha está vazia.
    """
    def __init__(self):
        self.topo = None

    def esta_vazia(self) -> bool:
        """Verifica se a pilha está vazia."""
        return self.topo is None

    def empilhar(self, item: any) -> None:
        """Adiciona um novo item ao topo da pilha."""
        novo_item = [item, self.topo]  # [item, proximo_topo]
        self.topo = novo_item

    def desempilhar(self) -> any:
        """Remove e retorna o item do topo da pilha."""
        if self.esta_vazia():
            raise Exception("Pilha vazia!")
        item_removido = self.topo[0]
        self.topo = self.topo[1]
        return item_removido

    def espiar(self) -> any:
        """Retorna o item do topo da pilha sem removê-lo."""
        if self.esta_vazia():
            raise Exception("Pilha vazia!")
        return self.topo[0]

    def tamanho(self) -> int:
        """Retorna o número de itens na pilha."""
        atual = self.topo
        contador = 0
        while atual:
            contador += 1
            atual = atual[1]
        return contador

    def imprime_pilha(self) -> None:
        """Imprime os itens da pilha do topo para a base."""
        atual = self.topo
        elementos = []
        while atual:
            elementos.append(str(atual[0]))
            atual = atual[1]
        print("Topo -> " + " -> ".join(elementos) + " -> Base")