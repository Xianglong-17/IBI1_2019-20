seq = 'ATGCGACTACGATCGAGGGCCAT' 
seq=seq.replace('A','t')
seq=seq.replace('T','a')
seq=seq.replace('C','g')
seq=seq.replace('G','c')#These steps are tp prevent multiple tranformation.
print(seq.upper())
