import pandas as pd


def ma_1(df: pd.DataFrame) -> None:
    print("=" * 70)
    print("MICROATIVIDADE 1) DATAFRAME ORIGINAL")
    print("=" * 70)
    print("\n" + df.to_string(index=False))
