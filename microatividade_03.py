import pandas as pd


def ma_3(df: pd.DataFrame) -> None:
    pd.set_option('display.max_rows', 9999)
    print("\n" + "=" * 70)
    print("MICROATIVIDADE 3) display.max_rows = 9999 E IMPRESSÃO VIA to_string()")
    print("=" * 70)
    print("\n" + df.to_string(index=False))
