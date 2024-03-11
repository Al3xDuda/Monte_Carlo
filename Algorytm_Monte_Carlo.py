import numpy as np
import matplotlib.pyplot as plt
import time

np.random.seed(111)
#try different numerical estimations?
def Monte_Carlo_PI(n): #n - number of points to draw
    def boundry_values(x):
        return np.sqrt(1-x*x)
    #n - number of points to draw
    x=np.random.uniform(0,1,n)
    y=np.random.uniform(0,1,n)
    #try different sampling methods?
    within=y<boundry_values(x)
    pi=4*sum(within)/n
    return [pi,x,y,within]

def Scatter_Plot_Monte_carlo(x,y,points_within):
    plt.scatter(x[points_within], y[points_within], color='purple', label='Within Area')
    plt.scatter(x[~points_within], y[~points_within], color='yellow', label='Outside Area')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Monte Carlo Simulation for π Estimation')
    plt.legend()
    plt.show()

start_time=time.time()
[pi,x,y,points_within]=Monte_Carlo_PI(100000)
Scatter_Plot_Monte_carlo(x,y,points_within)
end_time=time.time()
print(f"Compilation time: {end_time-start_time} seconds.")
print(f'Pi estimate value: {pi}')

#Plotting


