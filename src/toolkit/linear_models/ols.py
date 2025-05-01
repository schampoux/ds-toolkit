from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np 
from typing import DefaultDict
    
def x_y(df, feature_name: str, target_name: str)-> tuple[pd.DataFrame, pd.Series]:
    """
    Defines the features matrix and target array for OLS model instantiation.
    """
    
    x = np.array(df[feature_name])
    add_axis = x[:,np.newaxis]
    
    features_matrix = pd.DataFrame(add_axis, columns = target_name)
    target_array = pd.Series(df[target_name])

    print(f"Created features matrix with shape {features_matrix.shape} and target array with shape {target_array.shape}.")

    return features_matrix, target_array

def create_model(features_matrix, target_array):
    ols_inst = LinearRegression()
    ols_fit = ols_inst.fit(features_matrix, target_array)
    return ols_fit
    