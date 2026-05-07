import pandas as pd
import numpy as np

df = pd.read_excel('Vendas.xlsx')

df = df.dropna(subset=['Data da Venda', 'PrecoUnitario', 'Qtd. Vendida'])

df['Faturamento'] = df['PrecoUnitario'] * df['Qtd. Vendida']

faturamento_total = df['Faturamento'].sum()

produto_lider = df.groupby('Produto')['Faturamento'].sum().idxmax()

faturamento_marca = df.groupby('Marca')['Faturamento'].sum().sort_values(ascending=False).head(7)

df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])
evolucao_mensal = df.groupby(df['Data da Venda'].dt.to_period('M')).agg({
    'Faturamento': 'sum',
    'Qtd. Vendida': 'sum'
}).reset_index()

print(f"Faturamento Total: ${faturamento_total/1e6:.2f} Mi")
print(f"Produto mais vendido: {produto_lider}")
print("\nTop Marcas por Faturamento:")
print(faturamento_marca)