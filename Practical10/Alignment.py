seq1 = "MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq2 = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
seq3 = "WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"
edit_distance =	0 
for	i in range(len(seq1)): 
    if seq1[i] != seq2[i]:
        edit_distance += 1 
print("The human sequence is "+seq1)
print("The mouse sequence is "+seq2)
result="The percentage identity of human sequence and mouse sequence is "+str(100-edit_distance/len(seq1)*100)+"%"
print(result)
#The comparison between human sequence and mouse sequence.
edit_distance =	0 
for	i in range(len(seq3)): 
    if seq3[i] != seq1[i]:
        edit_distance += 1 
print("The human sequence is "+seq1)
print("The random sequence is "+seq3)
result="The percentage identity of human sequence and random sequence is "+str(100-edit_distance/len(seq3)*100)+"%"
print(result)
#The comparison between human sequence and random sequence.
edit_distance =	0 
for	i in range(len(seq2)): 
    if seq3[i] != seq2[i]:
        edit_distance += 1 
print("The mouse sequence is "+seq2)
print("The random sequence is "+seq3)
result="The percentage identity of random sequence and mouse sequence is "+str(100-edit_distance/len(seq1)*100)+"%"
print(result)
#The comparison between mouse sequence and random sequence.