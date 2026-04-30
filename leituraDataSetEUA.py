import pandas as pd
import os

os.system("cls")

caminho = r"C:\Users\dorfb\OneDrive\Documentos\TCC\datasets\ibtracs_USA_formatado.csv"

cols = ['LATITUDE', 'LONGITUDE']

# df = pd.read_csv(caminho, sep=',', low_memory=False)

# print(f"Total de registros: {len(df):,}")
# print(f"Colunas: {df.columns.tolist()}")
# print()
# print(df.head(60))

# Latitudes e longitudes estão como string, precisamos converter para float 
df = pd.read_csv(caminho, low_memory=False, usecols=cols)

# df = pd.read_csv(caminho, low_memory=False, parse_dates=['DATA_HORA'])

# print(f"Total de registros : {len(df):,}")
# print(f"Período            : {df['DATA_HORA'].min()} até {df['DATA_HORA'].max()}")
# print(f"Total de furacões  : {df['ID'].nunique()}")
print()
print(df.head(60))