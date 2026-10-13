# Trabalho Prático - DGT2823: Tecnologias para desenvolvimento de soluções de Big Data
# Objetivo: leitura, inspeção e limpeza de dados usando Pandas.
# Execute na pasta do projeto: python tratamento_dados.py
# Nome: Robson Batista Neto
# Matricula: 202501378005
# Curso: Desenvolvimento Full Stack
# resultado da execução pode ser conferido em result.txt

import pandas as pd

from microatividade_01 import ma_1
from microatividade_02 import ma_2
from microatividade_03 import ma_3
from microatividade_04 import ma_4
from microatividade_05 import ma_5
import servicos

ARQUIVO_CSV = "dados_exercicio.csv"

def main() -> None:
    df = servicos.read_csv(ARQUIVO_CSV)
    ma_1(df)
    ma_2(df)
    ma_3(df)
    ma_4(df)
    ma_5(df)

    df_tratado = servicos.limpar_calories(df)
    df_tratado = servicos.tratar_date(df_tratado)
    df_tratado = servicos.remover_nulos(df_tratado)
    servicos.salvar(df_tratado, "dados_tratados.csv")

if __name__ == "__main__":
    main()
