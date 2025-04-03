import pandas as pd
import numpy as np

def matrix_extractor(arquivo_excel):
    
    # Definir a linha e coluna inicial (começando de 0)
    linha_inicio = 2  # Exemplo: começa na 3ª linha (índice 2)
    coluna_inicio = 2  # Exemplo: começa na 2ª coluna (índice 1)

    # Ler a planilha 
    df = pd.read_excel(arquivo_excel, header=None)

    # Selecionar os dados a partir da linha e coluna especificadas
    df_recortado = df.iloc[linha_inicio:, coluna_inicio:]

    # Converter para NumPy array
    
    matriz_numpy = df_recortado.to_numpy(dtype=float) 

    # Exibir a matriz
    return matriz_numpy


def topsis(matriz, pesos, tipos_criterios):
    pesos = np.array(pesos)

    # normaliza a matriz
    matriz_norm = matriz / np.sqrt((matriz ** 2).sum(axis=0))
    
    #multiplica pelos pesos
    matriz_pesada = matriz_norm * pesos
    
    # determinar as soluções ideal positiva e negativa
    ideal_positivo = np.zeros(matriz.shape[1])
    ideal_negativo = np.zeros(matriz.shape[1])

    for i in range(matriz.shape[1]):
        if tipos_criterios[i] == 'max':  # Critério de benefício
            ideal_positivo[i] = matriz_pesada[:, i].max()
            ideal_negativo[i] = matriz_pesada[:, i].min()
        else:  # Critério de custo
            
            ideal_positivo[i] = matriz_pesada[:, i].min()
            ideal_negativo[i] = matriz_pesada[:, i].max()
    
    #calcular as distâncias
    distancia_positivo = np.sqrt(((matriz_pesada - ideal_positivo) ** 2).sum(axis=1))
    distancia_negativo = np.sqrt(((matriz_pesada - ideal_negativo) ** 2).sum(axis=1))
    
    # calcula o escore TOPSIS
    escore_topsis = distancia_negativo / (distancia_positivo + distancia_negativo)
    print(escore_topsis)
    escore_topsis= escore_topsis.reshape(-1, 1)
    print(escore_topsis)
    # ordena as alternativas pelo escore
    indices = np.arange(escore_topsis.shape[0]).reshape(-1, 1)
    matriz_nova = np.hstack((indices, escore_topsis))

    print(matriz_nova)
   # Ordenar a matriz pela coluna 0 (índices)
    matriz_ordenada = matriz_nova[np.argsort(matriz_nova[:, 1])[::-1]] #ordem decrescente

    print("Matriz ordenada")
    print(matriz_ordenada)  
    ranking = np.delete(matriz_ordenada, 1, axis=1)
    
    return ranking, escore_topsis

# Matriz de decisão (linhas = alternativas, colunas = critérios)
def critic(X):
    print(X)
    #define quais os critérios de benefício e custo
    benefit_criteria = [0, 2, 3, 4, 6, 7, 8, 9,10]  
    cost_criteria = [1, 5]  
    #normaliza matriz
    X_norm = np.zeros_like(X, dtype=float)

    for j in range(X.shape[1]):
        X_min = np.min(X[:, j])
        X_max = np.max(X[:, j])
        
        if j in benefit_criteria:
            X_norm[:, j] = (X[:, j] - X_min) / (X_max - X_min)
        elif j in cost_criteria:
            X_norm[:, j] = (X[:, j]) - X_max / (X_min - X_max)

    # Calcula do desvio padrão dos critérios
    sigma = np.std(X_norm, axis=0, ddof=0)

    # Matriz de correlação
    R = np.corrcoef(X_norm, rowvar=False)
   
    # Medida de informação Cj
    C = sigma * np.sum(1 - R, axis=0)
   
    # Pesos normalizados
    w = C / np.sum(C)

    # Exibir pesos
    for i, peso in enumerate(w):
        print(f'Critério {i+1}: {peso:.4f}')
    return w 
def cria_excel(matriz, nome_arquivo):
# Criar um DataFrame do Pandas
    df = pd.DataFrame(matriz,columns=[f"Ranking {nome_arquivo}"])

# Salvar como arquivo Excel
    caminho = f"/Users/mariana/Documents/1s25/EM993/Microcontroller_MCDM/DATA/{nome_arquivo}.xlsx"
    df.to_excel(caminho, index=False)
    print("fim")

