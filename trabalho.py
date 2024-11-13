import csv
import pandas as pd
import numpy as np

# 1 Leitura e Preparação dos Dados:
# Carregue os dados do arquivo CSV para um array numpy. Cada linha do dataset deve ser representada por um array unidimensional, e o dataset completo deve ser uma matriz 2D.
arquivo = pd.read_csv('vendas.csv')
arquivo_array = arquivo.values
print(arquivo_array)

# 2 Análise Estatística:
# Calcule a média, mediana e desvio padrão do Valor Total das vendas.
a=[]
b=[]
for i in range(len (arquivo_array)):
    a.append(arquivo_array[i][-1])
    b.append(arquivo_array[i][3])

media = np.mean(a)
mediana = np.median(a)
desvio = np.std(a)

print(media)
print(mediana)
print(desvio)

# Encontrar o produto com maior valor total de vendas
max_valor = np.max(a)
produto_maior_valor = None

for i in range(len(arquivo_array)):
    if arquivo_array[i][5] == max_valor:
        produto_maior_valor = arquivo_array[i][2]
        break
        
print(f"Produto com o maior valor total de vendas: {produto_maior_valor}")

# Encontrar o produto com a maior quantidade vendida
produtos = {}
for i in range(len(arquivo_array)):
    produto = arquivo_array[i][2]
    quantidade = arquivo_array[i][3]
    if produto in produtos:
        produtos[produto] += quantidade 
    else:
        produtos[produto] = quantidade

produto_maior_quantidade = max(produtos, key=produtos.get)
print(f"Produto com a maior quantidade vendida: {produto_maior_quantidade}")

# Calcular o valor total de vendas por região
vendas_por_regiao = {}
for i in range(len(arquivo_array)):
    regiao = arquivo_array[i][1]
    valor = arquivo_array[i][5]
    if regiao in vendas_por_regiao:
        vendas_por_regiao[regiao] += valor
    else:
        vendas_por_regiao[regiao] = valor

print("Valor total de vendas por região:")
for regiao, total in vendas_por_regiao.items():
    print(f"{regiao}: {total}")

# Calcular a venda média por dia
vendas_por_dia = {}
for i in range(len(arquivo_array)):
    data = arquivo_array[i][0]
    valor = arquivo_array[i][5]
    if data in vendas_por_dia:
        vendas_por_dia[data] += valor
    else:
        vendas_por_dia[data] = valor

venda_media_por_dia = np.mean(list(vendas_por_dia.values()))
print(f"Venda média por dia: {venda_media_por_dia}")

# 3 Análise Temporal:
# Determine o dia da semana com maior número de vendas.
dados = pd.DataFrame(arquivo_array, columns=['Data', 'Produto', 'Quantidade', 'ValorUnitario', 'Regiao', 'ValorTotal'])
dados['Data'] = pd.to_datetime(dados['Data'])
vendas_por_dia_da_semana = dados['Data'].dt.day_name().value_counts()
dia_com_mais_vendas = vendas_por_dia_da_semana.idxmax()
print(f'Dia da semana com maior número de vendas: {dia_com_mais_vendas}')

# Calcular a variação diária no valor total das vendas
pd.set_option('future.no_silent_downcasting', True)
vendas_por_dia = dados.groupby('Data')['ValorTotal'].sum()
variacao_diaria_vendas = vendas_por_dia.diff().fillna(0)
print('Variação diária no valor total das vendas:')
print(variacao_diaria_vendas)

# 4 Desafios Adicionais (Opcional):
# Função para retornar o total de vendas por região e produto
def total_vendas_regiao_produto(df, regiao, produto):
    filtro = (df['Regiao'] == regiao) & (df['Produto'] == produto)
    total_vendas = df.loc[filtro, 'ValorTotal'].sum()
    return total_vendas

# Exemplo de uso
regiao = 'Sudeste'
produto = 'Produto A'
total = total_vendas_regiao_produto(dados, regiao, produto)
print(f'Total de vendas para {produto} na região {regiao}: {total}')

# Função para analisar o crescimento das vendas ao longo do tempo
def crescimento_vendas(df, periodo1, periodo2):
    df['Data'] = pd.to_datetime(df['Data'])
    vendas_periodo1 = df[df['Data'].dt.to_period('M') == periodo1]['ValorTotal'].sum()
    vendas_periodo2 = df[df['Data'].dt.to_period('M') == periodo2]['ValorTotal'].sum()
    crescimento_percentual = ((vendas_periodo2 - vendas_periodo1) / vendas_periodo1) * 100
    return crescimento_percentual

# Exemplo de uso
periodo1 = '2024-01'
periodo2 = '2024-02'
crescimento = crescimento_vendas(dados, periodo1, periodo2)
print(f'Crescimento das vendas de {periodo1} para {periodo2}: {crescimento:.2f}%')