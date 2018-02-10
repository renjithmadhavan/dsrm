import matplotlib.pyplot as plt
import numpy as np


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

