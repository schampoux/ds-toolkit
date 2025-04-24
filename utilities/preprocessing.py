import pandas as pd

def remove_nans(df) -> pd.DataFrame:
    df["row_contains_nan"] = df.isnull().any(axis=1)
    df_no_nans = df[~df["row_contains_nan"]]
    output = df_no_nans.drop(columns = "row_contains_nan")
    df_no_nans = output
    print(f"\nRows with NaN's removed\n")
    return df_no_nans

def eda_nans(df):
    print("Number of NaN observations in each column.\n")
    for i in df.columns:
        print(i, sum(df[i].isnull()))
    print("\n")