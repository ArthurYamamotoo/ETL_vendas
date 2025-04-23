import pandas as pd
import psycopg2

df_clientes = pd.read_excel('vendas_loja_completa.xlsx', sheet_name='clientes')
df_vendas = pd.read_excel('vendas_loja_completa.xlsx', sheet_name='vendas')

df_clientes.dropna(subset=['id_cliente', 'nome'], inplace=True)

df_vendas.dropna(subset=['id_venda', 'id_cliente', 'data_venda', 'valor'], inplace=True)

df_clientes.drop_duplicates(subset='id_cliente', inplace=True)
df_vendas.drop_duplicates(subset='id_venda', inplace=True)

df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'], errors='coerce')

df_clientes['documento'] = df_clientes['documento'].astype(str).str.replace(r'\D', '', regex=True)

df_clientes['nome'] = df_clientes['nome'].str.title()

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="vendas_db",
    user="postgres",
    password="442085563"
)
cur = conn.cursor()

for _, row in df_clientes.iterrows():
    cur.execute("""
        INSERT INTO clientes (id_cliente, nome, email, documento, tipo_pessoa, tipo_contato)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id_cliente) DO NOTHING
    """, tuple(row))

for _, row in df_vendas.iterrows():
    cur.execute("""
        INSERT INTO vendas (id_venda, id_cliente, data_venda, valor)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id_venda) DO NOTHING
    """, tuple(row))

cur.execute("SELECT COUNT(*) FROM clientes")
print("Total de clientes inseridos:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM vendas")
print("Total de vendas inseridas:", cur.fetchone()[0])

conn.commit()
cur.close()
conn.close()
print("ETL finalizado com sucesso!")
