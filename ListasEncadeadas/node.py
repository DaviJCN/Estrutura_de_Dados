class Node:
    """
    Classe Node para listas encadeadas.
    Cada nó contém um valor (item) e uma referência para o próximo nó.
    """
    def __init__(self, item: any):
        self.item = item
        self.next = None

    def __repr__(self):
        return f"Node({self.item})"
