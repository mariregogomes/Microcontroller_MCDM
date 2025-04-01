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
])'''
print("Matriz extraída do excel \n")
print(matrix)

#Cálculo dos pesos usando o método critic, necessário colocar dentro da funcao os tipos de criterio
#vetor de pesos
vector_w=func.critic(matrix) 
print("Pesos\n")
print(vector_w)
#vector_w =np.array([0.35, 0.30, 0.35]) 
tipos_criterios = ['max', 'min', 'max', 'max', 'max', 'max', 'min', 'max', 'max', 'max', 'max', 'max'] 
#tipos_criterios = ['min','min', 'max']
ranking, escore = func.topsis(matrix, vector_w, tipos_criterios)

print("Escore \n")
print(escore)
print(ranking)
func.cria_excel(ranking+1, "Topsis")
print("Ranking TOPSIS \n")
for i, posicao in enumerate(ranking):
    print(f'Microcontrolador {i+1}: {posicao}')
