def conv(str):
        "Convert input DNA sequence to mRNA sequence"
        str=str.replace('A','U')
        str=str.replace('T','A')
        str=str.replace('C','g')
        str=str.replace('G','c')#These steps are to prevent multiple tranformation.
        print("The mRNA sequence is "+str.upper())
        return