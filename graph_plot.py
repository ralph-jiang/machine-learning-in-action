import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def plot_scatter_2D(x1,x2, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x1, x2, 15.0*np.array(y), 15.0*np.array(y))
    ax.axis([-2, 25, -0.2, 2.0])
    plt.xlabel('Percentage of Time Spent Playing Video Games')
    plt.ylabel('Liters of Ice Cream Consumed Per Week')
    plt.show()