import pandas as pd

class Prep():

    def __init__(self, df):
        self.df = df

    def remove_nans(self) -> pd.DataFrame:
        self.df["row_contains_nan"] = self.df.isnull().any(axis=1)
        df_no_nans = self.df[~self.df["row_contains_nan"]]
        output = df_no_nans.drop(columns = "row_contains_nan")
        self.df_no_nans = output
        return self.df_no_nans, print(f"\nNaN's removed from data via {Prep.remove_nans.__name__} method.\n")
    
    def eda_nans(self):
        print("Number of NaN observations in each column.\n")
        for i in self.df.columns:
            print(i, sum(self.df[i].isnull()))
        print("\n")

    def encode_categoricals(df: pd.DataFrame ):
        pass 

    def scale_features():
        pass