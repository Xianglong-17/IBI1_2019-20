import re
list=[]
list1=[]
mito_genes=[]
genes=''
name=''
length=''
seq=''
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
for line in xfile:
    genes=genes+line
    list=genes.split('>')
    
for i in list:
    if re.search('chromosome:R64-1-1:Mito:',i):
        mito_genes=mito_genes+[i]
for j in mito_genes:
    k = re.sub(r'\n','',j)
    name=re.sub(r'.+gene:(\S+).+',r'\1',k)
    seq=re.sub(r'.+](\S+)',r'\1',k)
    length=len(seq)
    list1=list1+[name+' '+str(length)+'\n'+seq]
 
yfile=open('mito_gene.fa','w')
for gene in list1:
    yfile.write(gene+'\n')
yfile.close()

print('success')