import pandas as pd 
from sklearn.linear_model import LinearRegression
from utilities.preprocessing import remove_nans, eda_nans
from linear_models.ols import x_y, create_model 

def main():
    # load in data 
    df = pd.read_csv('./datasets/babies.csv')
    
    # investigate nans 
    eda_nans(df = df)

    # remove nans
    df = remove_nans(df = df)
    feature = df.gestation.name 
    target = df.age.name
    # features matrix as pd.DataFrame, target_array as pd.Series
    features_matrix, target_array = x_y(df = df, feature_name = feature, target_name = target)
    print(features_matrix, target_array)

if __name__ =="__main__":
    main()
