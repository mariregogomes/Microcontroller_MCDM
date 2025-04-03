import numpy as np

# Criando uma matriz de exemplo (uma coluna)
matriz = np.array([[10], [5], [8], [3], [12]])

# Criar um array de índices das linhas e concatenar com a matriz original
indices = np.arange(matriz.shape[0]).reshape(-1, 1)
matriz_nova = np.hstack((indices, matriz))
print(matriz_nova)

# Ordenar a matriz pela coluna 1 (valores originais)
matriz_ordenada = matriz_nova[np.argsort(matriz_nova[:, 1])]

# Exibir a matriz final
print(matriz_ordenada)
