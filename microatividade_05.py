import pandas as pd


def ma_5(df: pd.DataFrame) -> None:
    print("\n" + "=" * 70)
    print("MICROATIVIDADE 5) EXIBIR INFORMAÇÕES GERAIS SOBRE O DATAFRAME")
    print("=" * 70 + "\n")
    df.info()
    print(f"\nTotal de linhas: {df.shape[0]}")
    print(f"Total de colunas: {df.shape[1]}")
    print("\nValores nulos por coluna:")
    print(df.isnull().sum())
    print("\nTipos de dados:")
    print(df.dtypes)
    print(f"\nMemória utilizada: {df.memory_usage(deep=True).sum()} bytes")
