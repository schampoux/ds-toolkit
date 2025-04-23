import matplotlib.pyplot as plt 
import numpy as np 

class Plotter():
    def __init__(self, model_instance):
        self.x = model_instance.features_matrix 
        self.y = model_instance.target_array
        self.x_label = self.x.name
        self.y_label = self.y.name 

    def scatter(self):
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y)
        ax.set_title(f"{self.x.name} vs {self.y.name}")
        fig.show() 
