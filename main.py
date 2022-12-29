import pandas as pd
import psycopg2
import config

db_conn_test = psycopg2.connect(host=config.DB_TESTE_HOST, dbname=config.DB_TESTE_NAME , user=config.DB_TESTE_USER, password=config.DB_TESTE_PASS)
# cursor_test = db_conn_test.cursor(cursor_factory=psycopg2.extras.DictCursor)

db_conn_risk = psycopg2.connect(host=config.DB_RISK_HOST, dbname=config.DB_RISK_NAME , user=config.DB_RISK_USER, password=config.DB_RISK_PASS)
# cursor_risk = db_conn_risk.cursor(cursor_factory=psycopg2.extras.DictCursor)

db_conn_kapv1 = psycopg2.connect(host=config.DB_KAPV1_HOST, dbname=config.DB_KAPV1_NAME , user=config.DB_KAPV1_USER, password=config.DB_KAPV1_PASS)
# cursor_kapv1 = db_conn_kapv1.cursor(cursor_factory=psycopg2.extras.DictCursor)

def main():
    return

def get_posicao(mercado,codigo):

    query=f"SELECT  str_fundo,SUM(dbl_lote) ,str_codigo \
            FROM public.tbl_carteira1 where str_mercado='{mercado}' and str_codigo='{mercado}' \
            group by str_fundo,str_codigo,str_codigo"
    df =pd.read_sql(query)
    return



if __name__ =='__main__':
    main()



