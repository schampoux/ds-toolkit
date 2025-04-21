from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np 

class SLR():
    
    def __init__(self, df: pd.DataFrame):
        self.df = df 

    def x_y(self, feature: str, target: str):
        """
        Defines the features matrix and target array to create the model for simple linear regression 
        """
        x = np.array(self.df[feature])
        
        self.features_matrix = x[:,np.newaxis]
        self.target_array = np.array(self.df[target])

        print(f"Created features matrix with shape {self.features_matrix.shape} and target array with shape {self.target_array.shape}.")
        return self.features_matrix, self.target_array

    def create_model(self):
        slr_model = LinearRegression()
        self.slr_model = slr_model.fit(self.features_matrix, self.target_array)
        return self.slr_model