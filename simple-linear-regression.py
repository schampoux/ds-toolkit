import pandas as pd 
from sklearn.linear_model import LinearRegression
from preprocessing import Prep
from linear_models.slr import SLR

def main():
    df = pd.read_csv('./datasets/babies.csv')
    prep_instance = Prep(df = df)
    prep_instance.remove_nans()
    data = prep_instance.df_no_nans

    slr_instance = SLR(df=data)
    feature = data.gestation.name 
    target = data.age.name 
    x, y = slr_instance.x_y(feature = feature, target=target)
    slr_model = slr_instance.create_model()
    print(slr_model)

if __name__ =="__main__":
    main()
