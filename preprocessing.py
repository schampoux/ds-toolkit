import pandas as pd

class Prep():
    def __init__(self, df):
        self.df = df

    def encode_categoricals(df: pd.DataFrame ):
        pass 

    def scale_features():
        pass

    def remove_nans(self) -> pd.DataFrame:
        self.df["row_contains_nan"] = self.df.isnull().any(axis=1)
        df_no_nans = self.df[~self.df["row_contains_nan"]]
        output = df_no_nans.drop(columns = "row_contains_nan")
        return output, print("nans removed")