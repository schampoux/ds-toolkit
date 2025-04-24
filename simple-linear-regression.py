import pandas as pd 
from sklearn.linear_model import LinearRegression
from utilities.preprocessing import remove_nans, eda_nans
from linear_models.ols import OLS




def main():
    df = pd.read_csv('./datasets/babies.csv')
    eda_nans(df)
    df = remove_nans(df)
    # ols_instance = OLS(df=data)
    # feature = data.gestation.name 
    # target = data.age.name 
    # ols_instance.x_y(feature = feature, target=target)
    # ols_model = ols_instance.create_model()
    # print("OLS model created with the following default attributes: ", "\nrank_", "\ncoef_", "\nsingular_", "\nintercept","\nn_features_in_")

if __name__ =="__main__":
    main()
