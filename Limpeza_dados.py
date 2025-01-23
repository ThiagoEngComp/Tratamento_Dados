import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

#Remover código
df.drop('pais', axis=1, inplace=True) #coluna
df.drop(2, axis=0, inplace=True) #Linha

#Normalizar Compos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()
print(df)

#Converte tipo de dados
df['idade'] = df['idade'].astype(int)

print('Normalizar textos',df.head())

#Tratar campos nulos (ausentes)
df_fillna = df.fillna(0) #Substituir valores nulos por 0
df_dropna = df.dropna() #Remover registro nulos
df_dropna4 = df.dropna(thresh=4) #Manter registro com cpf nulos
df = df.dropna(subset=['cpf'])#Remover registro cpf nulo

print('valores nulos \n', df.isnull().sum())
print('Qtd de registros nulos com fillna:', df_dropna.isnull().sum().sum())
print('Qtd de registros nulos com dropna:', df_dropna.isnull().sum().sum())
print('Qtd de registros nulos com dropna4:', df_dropna4.isnull().sum().sum())
print('Qtd de registros nulos com cpf:', df.isnull().sum().sum())

df.fillna(value={'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereco não encontrao')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

#Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%y', errors='coerce')

#Tratar dados duplicados
print('Qtd registros atual:', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd de registros removendo as duplicadas:', len(df))

print('Dados Limpos:\n', df)

#Salvar ddataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))