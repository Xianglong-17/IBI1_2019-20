import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/users/41145")
covid_data = pd.read_csv("full_data.csv")# importing the .csv ﬁle 
print(covid_data)
covid_data.iloc[0:16,::3]#showing all rows, and every third column between (and including) 0 and 15 
print(covid_data.iloc[0:16,::3])
covid_data.loc[:,"location"]# read just the “location” column, but all the rows from covid_data
print(covid_data.loc[:,"location"])
list=[]
for i in range(0,7996):
    if covid_data.loc[i,"location"]=='Afghanistan':
        list.append(True)
    elif covid_data.loc[i,"location"]!='Afghanistan':
        list.append(False)
#create a Boolean that is True when the “location” is “Afghanistan”, but false otherwise
covid_data.loc[list,"total_cases"]
#pick out datas about Afghanistan.
list1=[]
for i in range(0,7996):
    if covid_data.loc[i,"location"]=='World':
        list1.append(True)
    elif covid_data.loc[i,"location"]!='World':
        list1.append(False)
covid_data.loc[list1,"new_cases"]
world_new_cases=covid_data.loc[list1,"new_cases"]#make an object for storage.
mean=np.mean(world_new_cases)#calculate the mean value
median=np.median(world_new_cases)#calculate the meadian
print("The mean is "+str(mean))
print("The median is "+str(median))

plt.boxplot(world_new_cases)
plt.xticks([1],["world new cases"])
plt.ylabel("disitribution")
plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=0.4)
plt.show#This part draws the boxplot

world_dates=covid_data.loc[list1,"date"]#stores the dates
plt.plot(world_dates, world_new_cases, 'ro')
plt.xticks(world_dates.iloc[0:len(world_dates):5],rotation=-90)
plt.ylabel("new cases")
plt.xlabel("date")
plt.show#This part plots the new cases.

world_deaths=covid_data.loc[list1,"total_deaths"]
plt.plot(world_dates, world_deaths, 'bo')
plt.xticks(world_dates.iloc[0:len(world_dates):5],rotation=-90)
plt.ylabel("deaths")
plt.ylabel("date")
plt.show#This part plots the new deaths.

list2=[]
for i in range(0,7996):
    if covid_data.loc[i,"location"]=='Afghanistan':
        list2.append(True)
    elif covid_data.loc[i,"location"]!='Afghanistan':
        list2.append(False)
china_cases=covid_data.loc[list2,"total_cases"]
china_deaths=covid_data.loc[list2,"total_deaths"]
china_dates=covid_data.loc[list2,"date"]
plt.plot(china_dates,china_cases,'bo')
plt.plot(china_dates,china_deaths,'ro')
plt.xticks(china_dates.iloc[0:len(world_dates):5],rotation=-90)
plt.xlabel('date')
plt.ylabel('number')
plt.show