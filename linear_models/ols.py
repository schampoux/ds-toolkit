from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np 
from typing import DefaultDict

class OLS():
    
    def __init__(self, df: pd.DataFrame):
        self.df = df 
        self.info_dict = DefaultDict()

    def x_y(self, feature: str, target: str):
        """
        Defines the features matrix and target array for SLR model instantiation./ 
        """
        
        x = np.array(self.df[feature])
        self.info_dict["feature"]["name"]
        self.features_matrix = x[:,np.newaxis]
        self.target_array = np.array(self.df[target])

        print(f"Created features matrix with shape {self.features_matrix.shape} and target array with shape {self.target_array.shape}.")
        return self.features_matrix, self.target_array

    def create_model(self):
        ols_inst = LinearRegression()
        self.ols_fit = ols_inst.fit(self.features_matrix, self.target_array)
        return self.ols_fit
    