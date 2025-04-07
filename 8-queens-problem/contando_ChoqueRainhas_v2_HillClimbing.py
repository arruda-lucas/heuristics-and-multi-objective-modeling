import random
from collections import Counter

def generate_neighbors(state):
    neighbors = []
    for col in range(len(state)):
        for row in range(len(state)):
            if state[col] != row:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def count_attacks(state):
    somas = [state[i] + i for i in range(len(state))]
    subtracoes = [state[i] - i for i in range(len(state))]

    contagem_horizontal = Counter(state)
    contagem_somas = Counter(somas)
    contagem_subtracoes = Counter(subtracoes)

    ataques = 0
    for count in contagem_horizontal.values():
        if count > 1:
            ataques += count - 1
    for count in contagem_somas.values():
        if count > 1:
            ataques += count - 1
    for count in contagem_subtracoes.values():
        if count > 1:
            ataques += count - 1

    return ataques

def hill_climbing():
    current_state = [random.randint(0, 7) for _ in range(8)]  # Estado inicial aleatório
    current_attacks = count_attacks(current_state)
    update_count = 0  # Contador de atualizações do estado

    while True:
        neighbors = generate_neighbors(current_state)
        best_neighbor = None
        best_attacks = current_attacks

        for neighbor in neighbors:
            attacks = count_attacks(neighbor)
            if attacks < best_attacks:
                best_attacks = attacks
                best_neighbor = neighbor

        if best_neighbor is None:
            break

        current_state = best_neighbor
        current_attacks = best_attacks
        update_count += 1
        print(f"Novo estado: {current_state}, Ataques: {current_attacks}")

        if current_attacks == 0:
            break

    return current_state, current_attacks, update_count

# Executando o algoritmo
total_attempts = 100  # Para aumentar a chance de encontrar uma solução
update_counts = []  # Lista para armazenar os números de atualizações

for _ in range(total_attempts):
    solution, attacks, updates = hill_climbing()
    update_counts.append(updates)
    if attacks == 0:
        print("Solução encontrada:", solution)
        break
else:
    print("Nenhuma solução encontrada após", total_attempts, "tentativas.")

print("Total de atualizações do estado:", sum(update_counts))
