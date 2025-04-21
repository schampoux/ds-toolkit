import pandas as pd 
from sklearn.linear_model import LinearRegression
from preprocessing import Prep

def main():
    df = pd.read_csv('./datasets/babies.csv')
    preprocess = Prep(df = df)
    preprocess.remove_nans()

if __name__ =="__main__":
    main()
