import numpy as np
import matplotlib.pyplot as plt

def plot_polygon(pol):
    
    n = pol.shape[0]
    dots = np.reshape(np.append(pol[:,:],pol[0,:]), [n+1,2])
    
    plt.figure(1, figsize=(3,3))
    plt.plot(dots[:,0],dots[:,1],lw=5)
    plt.grid()
    axis('equal');

def plot_solution(sol):
    
    steps = sol.shape[0]
    n = sol.shape[1]
    plt.figure(1, figsize=(8,8))
    
    initial = np.reshape(np.append(solution[0,:,:],solution[0,0,:]), [n+1,2])
    final = np.reshape(np.append(solution[steps-1,:,:],solution[steps-1,0,:]), [n+1,2])
    for i in xrange(0,n):
        bug = sol[:,i,:]
        plt.plot(bug[:,0], bug[:,1])
    
    plt.plot(initial[:,0],initial[:,1])
    plt.plot(final[:,0],final[:,1])
    axis('equal');