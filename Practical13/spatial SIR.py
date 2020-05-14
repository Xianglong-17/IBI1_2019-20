import numpy as np 
import matplotlib . pyplot as plt
# Import necessary libraries.
population = np. zeros ( (100 , 100) )
# Make array of all susceptible population.
outbreak = np.random. choice (range(100) ,2)
population [ outbreak [0] , outbreak [ 1 ] ] = 1
# Choose a random point to be the first infected person.
beta=0.3
gamma=0.05
# Set up variables.
plt.figure (figsize =(6 ,4) , dpi=150) 
plt.imshow( population , cmap='viridis', interpolation='nearest' )
for i in range (0,100):
    infectedIndex = np.where(population==1) # find infected points
    for i in range(len(infectedIndex[0])):# get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y): 
                    # Avoid infecting the infected person himself.
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # Avoid falling of an edge.
                        if population[xNeighbour,yNeighbour]==0:
                            # Only infect neighbours that are not already infected!
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        population[x,y]=np.random.choice(range(2),1,p=[1 - gamma,gamma])[0] + 1 
        # Recovery simulation.
    plt.figure ( figsize =(6 ,4) , dpi=150) 
    plt.imshow( population , cmap='viridis', interpolation='nearest')
    # Produce and ouotput the plot.