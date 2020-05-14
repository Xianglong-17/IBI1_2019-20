import numpy as np
import matplotlib.pyplot as plt
# Import neccessary libraries.
t = [0] # t represents time.
n = 10000 # n represents population.
β = 0.3
γ = 0.05
time = 1000 # We perform 1000 time loop in the programme.
for j in range (0,11): #j influences vaccination percentage.
    t = [0]
    sus = [int(n - 1 - (n * j / 10))] #Initial suspectible population.
    inf = [1] # Initial infected population.
    rec = [0] # Initial recovered population.
    if sus[0] < 0: # To set a checkpoint to stop.
        sus = [0]
        inf = [0]
    for i in range (0,time):
        a = np.random.choice(range(2),sus[i],p=[1-β*(inf[i]/n),β*(inf[i]/n)])
        num1 = np.sum(a == 1)
        b = np.random.choice(range(2),inf[i],p=[1-γ,γ])
        num2 = np.sum(b == 1)
        sus.append (sus[i] - num1)
        inf.append (inf[i] + num1 - num2)
        rec.append (rec[i] + num2)
        t.append (i) # Create the procedure for one loop.
    inf_1 = inf
    lab = str(j * 10) +'%'
    plt.plot(t, inf_1, label=lab)
    plt.legend(loc = 'upper right')
    # Produce and save data in different case.
plt.title('SIR model with different percentage of vaccination')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.savefig('SIR model', type='png' )
plt.show
# Create and save the plot.