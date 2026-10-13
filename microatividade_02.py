import pandas as pd


def ma_2(df: pd.DataFrame) -> pd.DataFrame:
    subset = df[["ID", "Date", "Calories"]].copy()
    print("\n" + "=" * 70)
    print("MICROATIVIDADE 2) SUBCONJUNTO DE 3 COLUNAS (ID, Date, Calories)")
    print("=" * 70)
    print("\n" + subset.to_string(index=False))
    return subset
