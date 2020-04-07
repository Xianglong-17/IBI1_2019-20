frequency= {'A':0,'T':0,'C':0,'G':0}
sequence="ATGCTTCAGAAAGGTCTTAGG"
frequency['A']=sequence.count('A')
frequency['C']=sequence.count('C')
frequency['G']=sequence.count('G')
frequency['T']=sequence.count('T')#count the frequency of each part
import matplotlib.pyplot as plt #import plt
dict={'A':5 , 'C':14 , 'G':7 , 'T':3}#create dictinary
labels=('A','C','G','T')
sizes=[dict['A'],dict["C"],dict['G'],dict['T']]
explode=(0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,
        startangle=90)
plt.axis('equal')#create details about pie chart
plt.show()
print(dict)#show the pie chart and print the dictionary