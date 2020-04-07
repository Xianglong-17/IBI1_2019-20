import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/users/41145")
covid_data = pd.read_csv("full_data.csv")# importing the .csv ﬁle 
covid_data.iloc[0:16,::3]#showing all rows, and every third column between (and including) 0 and 15 
covid_data.loc[:,"location"]# read just the “location” column, but all the rows from covid_data



