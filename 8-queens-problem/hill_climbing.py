"""Problema das 8 rainhas"""

import random 

def generate_neighbors(state):
    neighbors = []
    for col in range(len(state)):
        for row in range(len(state)):
            if state[col] != row:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

# Rainha da coluna i está na linha estado[i]
initial_state = [random.randint(0, 7) for _ in range(8)]

neighbors = generate_neighbors(initial_state)
print("Estado inicial:", initial_state)
print("Vizinhos gerados:", neighbors[20])

estado = [5, 5, 7, 6, 5, 1, 3, 0]

def ataques(estado):
    ataques = 0
    n = len(estado)

    #ataques na mesma linha
    for i in range(n):
        for j in range(i + 1, n):  # Evita comparar a mesma rainha e pares duplicados
            if estado[i] == estado[j]:
                ataques += 1
    return ataques

print(ataques(estado))