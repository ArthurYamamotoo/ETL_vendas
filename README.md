# ETL VENDAS

Projeto de processo ETL de um arquivo Excel que insere dados tratados em um BD.

# Para rodar e necessario clonar e  deppis criar um ambiente virtual

git clone ou baixar os arquivos na sua maquina
cd etl_vendas

python3 -m venv venv
source venv/bin/activate

# Instalar a dependencia

 pip install pandas openpyxl psycopg2-binary

 # Criar banco e tabelas

 Acessar PostgreSQL e executar o aquivo dump.sql para criação de tabela

 # executar o script
 python etl.py

01 - O script carrega automaticamnete os dados das abas clientes e vendas da planilha

02 - O script renomeia colunas inconsistentes e ingnora duplicatas antes de inserir no banco

03 - Tabela criada com CREATE TABLE

04 - Feito com ISERT INTO CONFLICT DO NOTHING, com interrows

