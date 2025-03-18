# ========================================
# Lista Simplesmente Encadeada
# ========================================

class Node:
    # Definindo o nó para lista simplesmente encadeada
    def __init__(self, data=None):
        self.data = data  # Armazena o valor do nó
        self.next = None  # Ponteiro para o próximo nó (inicialmente None)

class LinkedList:
    def __init__(self):
        self.head = None  # A cabeça da lista começa como None, indicando que a lista está vazia

    # Inserir no final da lista
    def insert(self, data):
        new_node = Node(data)  # Cria um novo nó com o dado fornecido
        if not self.head:  # Se a lista estiver vazia
            self.head = new_node  # O novo nó é a cabeça da lista
        else:
            temp = self.head
            while temp.next:  # Vai até o último nó
                temp = temp.next
            temp.next = new_node  # Conecta o novo nó ao último nó

    # Remover um nó
    def remove(self, data):
        temp = self.head
        if temp and temp.data == data:  # Se o nó a ser removido for o primeiro
            self.head = temp.next  # Faz a cabeça apontar para o próximo nó
            temp = None  # Remove o nó da memória
            return

        prev = None
        while temp and temp.data != data:  # Procura o nó com o valor fornecido
            prev = temp
            temp = temp.next

        if temp is None:  # Se o nó não for encontrado
            print("Elemento não encontrado")
            return

        prev.next = temp.next  # Desvincula o nó da lista
        temp = None  # Remove o nó da memória

    # Buscar um valor na lista
    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:  # Se encontrar o valor
                return True
            temp = temp.next
        return False  # Se não encontrar, retorna False

    # Atualizar um valor na lista
    def update(self, old_data, new_data):
        temp = self.head
        while temp:
            if temp.data == old_data:  # Se encontrar o nó com o valor a ser atualizado
                temp.data = new_data  # Atualiza o valor do nó
                return True
            temp = temp.next
        return False  # Se não encontrar, retorna False

    # Exibir os elementos da lista
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")  # Exibe o valor do nó
            temp = temp.next
        print("NULL")  # Indica o fim da lista

# ========================================
# Lista Duplamente Encadeada
# ========================================

class DNode:
    # Definindo o nó para lista duplamente encadeada (com ponteiro para o próximo e o anterior)
    def __init__(self, data=None):
        self.data = data  # Armazena o valor do nó
        self.next = None  # Ponteiro para o próximo nó
        self.prev = None  # Ponteiro para o nó anterior

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # A cabeça da lista começa como None, indicando que a lista está vazia

    # Inserir no final da lista
    def insert(self, data):
        new_node = DNode(data)  # Cria um novo nó com o dado fornecido
        if not self.head:  # Se a lista estiver vazia
            self.head = new_node  # O novo nó é a cabeça da lista
        else:
            temp = self.head
            while temp.next:  # Vai até o último nó
                temp = temp.next
            temp.next = new_node  # Conecta o novo nó ao último nó
            new_node.prev = temp  # Faz o ponteiro 'prev' do novo nó apontar para o nó anterior

    # Remover um nó
    def remove(self, data):
        temp = self.head
        if temp and temp.data == data:  # Se o nó a ser removido for o primeiro
            self.head = temp.next  # Faz a cabeça apontar para o próximo nó
            if self.head:  # Se a lista não estiver vazia, ajusta o ponteiro 'prev' do novo primeiro nó
                self.head.prev = None
            temp = None  # Remove o nó da memória
            return

        while temp and temp.data != data:  # Procura o nó com o valor fornecido
            temp = temp.next

        if temp is None:  # Se o nó não for encontrado
            print("Elemento não encontrado")
            return

        # Ajusta os ponteiros dos nós adjacentes para desvincular o nó da lista
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        temp = None  # Remove o nó da memória

    # Buscar um valor na lista
    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:  # Se encontrar o valor
                return True
            temp = temp.next
        return False  # Se não encontrar, retorna False

    # Atualizar um valor na lista
    def update(self, old_data, new_data):
        temp = self.head
        while temp:  # Percorre a lista
            if temp.data == old_data:  # Se encontrar o nó com o valor a ser atualizado
                temp.data = new_data  # Atualiza o valor do nó
                return True
            temp = temp.next
        return False  # Se não encontrar, retorna False

    # Exibir os elementos da lista
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")  # Exibe o valor do nó com a conexão dupla
            temp = temp.next
        print("NULL")  # Indica o fim da lista

# ========================================
# Exemplo de Uso para Ambas as Listas
# ========================================

# Lista Simplesmente Encadeada
print("Lista Simplesmente Encadeada:")
lista = LinkedList()
lista.insert(10)  # Insere 10
lista.insert(20)  # Insere 20
lista.insert(30)  # Insere 30
lista.display()  # Exibe: 10 -> 20 -> 30 -> NULL

lista.remove(20)  # Remove o valor 20
lista.display()  # Exibe: 10 -> 30 -> NULL

print(lista.search(10))  # Exibe: True (10 está na lista)
print(lista.search(20))  # Exibe: False (20 não está mais na lista)

lista.update(30, 40)  # Atualiza 30 para 40
lista.display()  # Exibe: 10 -> 40 -> NULL

print("\n")  # Pular linha

# Lista Duplamente Encadeada
print("Lista Duplamente Encadeada:")
dlist = DoublyLinkedList()
dlist.insert(10)  # Insere 10
dlist.insert(20)  # Insere 20
dlist.insert(30)  # Insere 30
dlist.display()  # Exibe: 10 <-> 20 <-> 30 <-> NULL

dlist.remove(20)  # Remove o valor 20
dlist.display()  # Exibe: 10 <-> 30 <-> NULL

print(dlist.search(10))  # Exibe: True (10 está na lista)
print(dlist.search(20))  # Exibe: False (20 não está mais na lista)

dlist.update(30, 40)  # Atualiza 30 para 40
dlist.display()  # Exibe: 10 <-> 40 <-> NULL
