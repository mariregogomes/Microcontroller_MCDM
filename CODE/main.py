import numpy as np
import func 

# Nome do arquivo Excel
arquivo_excel = "/Users/mariana/Documents/1s25/EM993/Microcontroller_MCDM/DATA/ProductsList.xlsx"  
matrix = func.matrix_extractor(arquivo_excel).astype(float)

'''
matrix=np.array([
    [100000.00, 0.12, 0.20],
    [80000.00, 0.11, 0.22],
    [85000.00, 0.14, 0.25],
    [110000.00, 0.20, 0.22],
    [200000.00, 0.30, 0.35],
    [150000.00, 0.15, 0.22],
    [95000.00, 0.07, 0.12],
    [130000.00, 0.13, 0.15],
    [120000.00, 0.12, 0.15],
    [90000.00, 0.15, 0.20]
])

matrix = np.array([
    [1, 2, 1, 1, 2, 1, 1, 3],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 3, 4, 1, 2, 4, 2, 1],
    [2, 2, 1, 3, 2, 3, 1, 1],
    [3, 2, 1, 2, 3, 1, 2, 1],
    [3, 2, 1, 2, 3, 1, 2, 1],
    [2, 1, 2, 2, 2, 1, 2, 3],
    [2, 3, 1, 3, 2, 2, 1, 1],
    [1, 1, 3, 2, 4, 1, 2, 1],
    [2, 2, 3, 3, 3, 2, 4, 4],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 2, 1, 2, 1, 1, 2],
    [1, 2, 2, 3, 3, 2, 2, 3],
    [3, 2, 2, 2, 2, 2, 3, 2],
    [4, 2, 2, 3, 2, 1, 3, 3],
    [2, 1, 2, 3, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 2],
    [2, 2, 1, 4, 4, 3, 2, 1],
    [2, 1, 1, 1, 2, 1, 1, 1],
    [2, 1, 2, 2, 2, 3, 1, 2]
])
'''
print("Matriz extraída do excel \n")
print(matrix)

#Cálculo dos pesos usando o método critic, necessário colocar dentro da funcao os tipos de criterio
#vetor de pesos
vector_w=func.critic(matrix).astype(float)
print("Pesos\n")
print(vector_w)
func.cria_excel(vector_w, "Pesos_Critic")
#vector_w =np.array([0.35, 0.30, 0.35]) 
tipos_criterios = ['max', 'min', 'max', 'max', 'max', 'min', 'max', 'max', 'max', 'max', 'max'] 
#tipos_criterios = ['min','min', 'max']

ranking, escore = func.topsis(matrix, vector_w, tipos_criterios)

print("Escore \n")
print(escore)
func.cria_excel(escore, "Escore_")
print(ranking)
func.cria_excel(ranking+1, "Topsis_")
print("Ranking TOPSIS \n")
for i, posicao in enumerate(ranking+1):
    print(f'{i+1}°: Microcontrolador {posicao}')
