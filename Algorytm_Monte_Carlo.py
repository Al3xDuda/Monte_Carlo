import pandas as pd
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
    plt.scatter(x[points_within], y[points_within], color='purple', label='Within Area',s=2)
    plt.scatter(x[~points_within], y[~points_within], color='yellow', label='Outside Area',s=2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Monte Carlo Simulation for π Estimation')
    plt.legend()
    plt.show()

def Perform_Simulations(N,n): #N - amount of simulations #n - amount of smaples in each simulation
    #columns- each simulation
    #index is number of samples. each value is essentaily a pi estimate in each simulation in with <index. amount of samples
    pi_estimate_array = pd.DataFrame(index=range(n), columns=range(N), dtype=float)
    pi_estimate_array.fillna(0, inplace=True)
    print(pi_estimate_array.head())
    # for i in range(0,n):
    #     for i in range(0,N):


start_time=time.time()
[pi,x,y,points_within]=Monte_Carlo_PI(10000)
Scatter_Plot_Monte_carlo(x,y,points_within)
end_time=time.time()
print(f"Compilation time: {end_time-start_time} seconds.")
print(f'Pi estimate value: {pi}')

#Plotting
Perform_Simulations(2,10)

