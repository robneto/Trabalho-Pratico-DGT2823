import pandas as pd


def ma_4(df: pd.DataFrame) -> None:
    print("\n" + "=" * 70)
    print("MICROATIVIDADE 4) EXIBIR AS PRIMEIRAS E ÚLTIMAS 10 LINHAS")
    print("=" * 70)
    print("\nPrimeiras 10 linhas:")
    print(df.head(10).to_string(index=False))
    print("\nÚltimas 10 linhas:")
    print(df.tail(10).to_string(index=False))
