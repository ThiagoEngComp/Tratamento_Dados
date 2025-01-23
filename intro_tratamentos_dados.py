import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar os primeiros registros
print('Inicio: ',df.head().to_string())# Inicio
print('Calda: ',df.tail().to_string())# calda

#Verificar qts linha e colunas
print('Quantidade de linhas e colunas: ',df.shape)

#Verificar tipo de dados
print('Tipo de dados:\n',df.dtypes)

# Checar valores nulos
print('Valores nulos:\n',df.isnull().sum())
