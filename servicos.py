import pandas as pd

ARQUIVO_CSV = "dados_exercicio.csv"

def read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep=";", engine="python", encoding="utf-8")

def limpar_calories(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    df2["Calories"] = pd.to_numeric(df2["Calories"], errors="coerce")
    df2["Calories"] = df2["Calories"].fillna(0)
    print("\n" + "=" * 70)
    print("APÓS SUBSTITUIR NULOS DE CALORIES POR 0")
    print("=" * 70 + "\n")
    print(df2.to_string(index=False))
    return df2

def tratar_date(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    # Normaliza strings e limpa aspas simples
    df2["Date"] = df2["Date"].astype("string").str.strip()
    df2["Date"] = df2["Date"].str.strip("'")
    df2["Date"] = df2["Date"].replace({"<NA>": pd.NA, "NaN": pd.NA, "": pd.NA})

    # Conforme roteiro: preencher temporariamente com '1900/01/01'
    df2["Date"] = df2["Date"].fillna("1900/01/01")
    print("\n" + "=" * 70)
    print("APÓS SUBSTITUIR DATA NULA POR 1900/01/01")
    print("=" * 70 + "\n")
    print(df2.to_string(index=False))

    # Troca o marcador temporário por NaN para permitir remoção posterior
    df2["Date"] = df2["Date"].replace("1900/01/01", pd.NA)

    # Trata valor compacto 20201226 -> YYYY/MM/DD
    df2["Date"] = df2["Date"].replace(
        "20201226",
        pd.to_datetime("20201226", format="%Y%m%d").strftime("%Y/%m/%d"),
    )

    # Converte para datetime
    df2["Date"] = pd.to_datetime(df2["Date"], format="%Y/%m/%d", errors="coerce")

    print("\n" + "=" * 70)
    print("APÓS NORMALIZAR E CONVERTER DATE PARA DATETIME")
    print("=" * 70 + "\n")
    print(df2.to_string(index=False))
    print("\nTipo da coluna Date:", df2["Date"].dtype)
    return df2

def remover_nulos(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.dropna(subset=["Date"]).copy()
    print("\n" + "=" * 70)
    print("DATAFRAME FINAL APÓS REMOVER DATAS NULAS")
    print("=" * 70 + "\n")
    print(df2.to_string(index=False))
    print(f"\nLinhas finais: {df2.shape[0]}")
    print(f"Colunas finais: {df2.shape[1]}")
    print("\nNulos por coluna após a limpeza:")
    print(df2.isnull().sum())
    return df2

def salvar(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, sep=";", index=False, encoding="utf-8")
    print(f"\nArquivo '{path}' gerado com sucesso.")
