import os
import re
os.chdir("/users/41145")
list=[]
mito_genes=[]
genes=''
name=''
length=''
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
for line in xfile:
    genes=genes+line
    list=genes.split('>')
    
for i in list:
    if re.search('chromosome:R64-1-1:Mito:',i):
        mito_genes=mito_genes+[i]
for j in mito_genes:
    name=re.sub(r'.+gene:(\S+).+',r'\1',j)
    length=