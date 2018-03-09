import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn import datasets
from sklearn import linear_model
from scipy.stats.stats import pearsonr
import math
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
warnings.filterwarnings("ignore", category = FutureWarning, module = "pandas.core.datetools")




def simplechart():
    print("""
    fig = plt.figure()
    ax = plt.axes()
    ax.plot(x, y, color='blue', linestyle='solid', label='plot1')
    #plt.axis([-1, 11, -1.5, 1.5])
    plt.title("A Sine Curve")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.axis('equal')
    plt.legend() 
    """)

def plot_multiline(x, pred, actual):
    fig = plt.figure(figsize=(12, 6))
    ax = plt.axes()
    ax.plot(x, pred, color='blue', linestyle='solid', label='pred')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.plot(x, actual, color='red', linestyle='dashed', label='actual')
    plt.title("Predicted Values")
    plt.xlabel("Independent Variable")
    plt.ylabel("Pred")
    #plt.axis('equal')
    plt.legend() 

