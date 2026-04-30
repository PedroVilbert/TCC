import pandas as pd
import os

os.system("cls")

caminho = r"C:\Users\dorfb\OneDrive\Documentos\TCC\ibtracs_USA.csv"

cols = ['SID', 'NAME', 'BASIN', 'NATURE', 'WMO_AGENCY', 'DIST2LAND', 'LANDFALL', 
        'SEASON', 'ISO_TIME', 'LAT', 'LON', 'USA_SSHS', 'USA_GUST', 
        'STORM_SPEED', 'STORM_DIR']

df = pd.read_csv(caminho, sep=',', usecols=cols, low_memory=False)

print(f"Total de registros: {len(df):,}")
print(f"Colunas: {df.columns.tolist()}")
print()
print(df.head(60))