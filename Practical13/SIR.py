import numpy as np
import matplotlib.pyplot as plt
# Import neccessary libraries.
t = [0] # t represents time.
n = 10000 # n represents population.
β = 0.3
γ = 0.05
time = 1000 # We perform 1000 time loop in the programme.
sus = [n- 1] # Initial suspectible population.
inf = [1] # Initial infected population.
rec = [0] # Initial recovered population.
for i in range (0,time-1):
    a = np.random.choice(range(2),sus[i],p=[1-β*(inf[i]/n),β*(inf[i]/n)])
    num1 = np.sum(a == 1)
    b = np.random.choice(range(2),inf[i],p=[1-γ,γ])
    num2 = np.sum(b == 1)
    sus.append (sus[i] - num1)
    inf.append (inf[i] + num1 - num2)
    rec.append (rec[i] + num2)
    t.append (i)
# Create the procedure for one loop.
plt.plot(t, sus, color='yellow', label='suspectible')
plt.plot(t, inf, color='red', label='infected')
plt.plot(t, rec, color='green', label='recovered')
plt.title('SIR model')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.legend(loc = 'upper right')
plt.savefig('SIR model', type='png' )
plt.show
# Create and save the plot.