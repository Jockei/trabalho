import csv
import pandas as pd
import numpy as np

#1
arquivo = pd.read_csv('vendas.csv')
arquivo_array = arquivo.values
print(arquivo_array)

#2
a=[]
b=[]
for i in range(len (arquivo_array)):
    a.append(arquivo_array[i][-1])
    b.append(arquivo_array[i][3])
    media = np.mean(a)
print(media)

mediana = np.median(a)
print(mediana)

desvio = np.std(a)
print(desvio)

max_valor = (np.max(a))

for i in range(len(arquivo_array)):
    if arquivo_array[i][5] == max_valor:
        print(arquivo_array[i][2])

produtoA = 0
produtoB = 0
produtoC = 0
for i in range(len(arquivo_array)):
    if arquivo_array[i][2] == "Produto A":
        produtoA += arquivo_array[i][3]
    if arquivo_array[i][2] == "Produto B":
        produtoB += arquivo_array[i][3]
    if arquivo_array[i][2] == "Produto C":
        produtoC += arquivo_array[i][3]
produtos = [produtoA, produtoB, produtoC]
max_quantidade = (np.max(produtos))

for i in range(len(arquivo_array)):
    if max_quantidade == produtos[i]:
        