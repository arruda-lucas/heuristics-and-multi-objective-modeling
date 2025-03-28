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

def count_repetitions(state):
    somas = [state[i] + (i + 1) for i in range(len(state))]
    subtracoes = [state[i] - (i + 1) for i in range(len(state))]

    contagem_horizontal = Counter(state)  # Contagem dos valores no estado inicial
    contagem_somas = Counter(somas)  # Contagem dos valores na lista somas
    contagem_subtracoes = Counter(subtracoes)  # Contagem dos valores na lista subtrações

    repetidos_horizontal = {key: value for key, value in contagem_horizontal.items() if value > 1}
    repetidos_somas = {key: value for key, value in contagem_somas.items() if value > 1}
    repetidos_subtracoes = {key: value for key, value in contagem_subtracoes.items() if value > 1}
    
    choque_rainhas_diagonal = sum((value - 1) for value in repetidos_somas.values())
    choque_rainhas_diagonal_contraria = sum((value - 1) for value in repetidos_subtracoes.values())
    choque_rainhas_horizontal = sum((value - 1) for value in repetidos_horizontal.values())
    
    return contagem_horizontal, contagem_somas, contagem_subtracoes, repetidos_horizontal, repetidos_somas, repetidos_subtracoes, choque_rainhas_horizontal, choque_rainhas_diagonal, choque_rainhas_diagonal_contraria

# Estado inicial aleatório
initial_state = [random.randint(0, 7) for _ in range(8)]
#initial_state = [5, 3, 1, 4, 0, 4, 5, 4]	
#initial_state = [0, 5, 7, 2, 6, 3, 1, 4]	#Possível solucao

# Obter contagens relevantes
contagem_horizontal, contagem_somas, contagem_subtracoes, repetidos_horizontal, repetidos_somas, repetidos_subtracoes, choque_rainhas_horizontal, choque_rainhas_diagonal, choque_rainhas_diagonal_contraria = count_repetitions(initial_state)

# Gerar os vizinhos
neighbors = generate_neighbors(initial_state)

# Exibição
print("\nEstado inicial:", initial_state)
#print("\nContagem de valores de número de linha + coluna:", contagem_somas)
#print("\nContagem de valores de número de linha - coluna:", contagem_subtracoes)
#print("\nContagem de valores do estado inicial:", contagem_horizontal)
#print("\nValores repetidos e suas ocorrências:", repetidos_horizontal)
#print(f"\nQuantidade de números repetidos: {len(repetidos_horizontal)}")   #Essa quantidade é realmente igual ao número de choques entre rainhas? VERIFICAR!
#print("\nValores repetidos e suas ocorrências:", repetidos_somas)
#print(f"\nQuantidade de números repetidos: {len(repetidos_somas)}")   #Essa quantidade é realmente igual ao número de choques entre rainhas? VERIFICAR!
#print("\nValores repetidos e suas ocorrências:", repetidos_subtracoes)
#print(f"\nQuantidade de números repetidos: {len(repetidos_subtracoes)}")   #Essa quantidade é realmente igual ao número de choques entre rainhas? VERIFICAR!
print(f"\nQuantidade de pares de rainhas que se atacam na horizontal: {choque_rainhas_horizontal}")
print(f"\nQuantidade de pares de rainhas que se atacam na diagonal principal: {choque_rainhas_diagonal}")
print(f"\nQuantidade de pares de rainhas que se atacam na diagonal secundária: {choque_rainhas_diagonal_contraria}")
print("\nVizinhos gerados:", neighbors)
