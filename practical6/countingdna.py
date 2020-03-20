#import plt
#create dictionary
#create details about pie chart
#show the pie chart and print the dictionary
import matplotlib.pyplot as plt 
dict={'A':5 , 'C':14 , 'G':7 , 'T':3}
labels='A','C','G','T'
sizes=[dict['A'],dict["C"],dict['G'],dict['T']]
explode=(0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,
        startangle=90)
plt.axis('equal')
plt.show()
print(dict)