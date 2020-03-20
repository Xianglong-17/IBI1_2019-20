
x=63 #have an integer x
while x!=1:
    print(x)#if x is even,devided by 2; if odd, multipy by 3 and add 1;if x=1, stop.
    if x%2==0:
        x=x/2
    elif x%2==1:
        x=x*3+1
print(x)