# --------------------------------------------
# LISTAS (Arrays Dinâmicos)
# --------------------------------------------

# Criação e manipulação
lista = [10, 20, 30, 40]

# Acesso por índice
print(lista[1])  # 20

# Slicing
print(lista[1:3])  # [20, 30]

# Métodos importantes
lista.append(50)           # [10, 20, 30, 40, 50]
lista.insert(2, 25)        # [10, 20, 25, 30, 40, 50]
lista.remove(25)           # [10, 20, 30, 40, 50]
lista.pop()                # remove o último
print(lista.index(20))     # posição do valor 20
print(lista.count(10))     # quantas vezes 10 aparece
lista.sort()               # ordena
lista.reverse()            # inverte
copia = lista.copy()       # cópia
lista.clear()              # esvazia

# List comprehensions
quadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Diferença entre lista e tupla
lista = [1, 2, 3]      # mutável
tupla = (1, 2, 3)      # imutável

# --------------------------------------------
# FILAS (Queues)
# --------------------------------------------

from collections import deque

# Conceito FIFO (First-In, First-Out)
fila = deque()

# enqueue
fila.append("A")
fila.append("B")

# dequeue
print(fila.popleft())  # A

# peek
print(fila[0])  # B

# is_empty
print(len(fila) == 0)

# size
print(len(fila))

# --------------------------------------------
# PILHAS (Stacks)
# --------------------------------------------

# Conceito LIFO (Last-In, First-Out)
pilha = []

# push
pilha.append("X")
pilha.append("Y")

# pop
print(pilha.pop())  # Y

# peek
print(pilha[-1])  # X

# is_empty
print(len(pilha) == 0)

# size
print(len(pilha))

# --------------------------------------------
# VETORES (Arrays unidimensionais)
# --------------------------------------------

import array

# Conceito: sequência de mesmo tipo
vetor = array.array('i', [1, 2, 3, 4])

# acesso
print(vetor[2])  # 3

# iteração
for num in vetor:
    print(num)

# --------------------------------------------
# MATRIZES (Arrays Bidimensionais)
# --------------------------------------------

# Representação com listas de listas
matriz = [
    [1, 2],
    [3, 4]
]

# Acesso: linha e coluna
print(matriz[1][0])  # 3

# Iteração
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")

# Soma de matrizes
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

soma = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print("Soma:", soma)

# Multiplicação conceitual
mult = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print("Multiplicação:", mult)

# Com NumPy (mais eficiente)
import numpy as np

np_A = np.array(A)
np_B = np.array(B)

print("NumPy Soma:\n", np_A + np_B)
print("NumPy Multiplicação (dot):\n", np.dot(np_A, np_B))
