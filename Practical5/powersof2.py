#write a number x;a string (result)
#compare x to different powers of 2.
#if x > 2**i and x < 2**(i+1),Xi=true x=x-2**i, continue.
x=1750
R=str(x)+" is "
for i in range(0,14):      
      if x>=2**(13-i) and x<2**(14-i):
        R=R+ "2**"+str(13-i)+ " + "
        x=x-2**(13-i)      
print(R.strip(' + '))#delete the extra ' + '