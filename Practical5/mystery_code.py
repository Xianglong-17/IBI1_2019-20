# What does this piece of code do?
# Answer: Spawn a random prime number between 1 and 100.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    n = randint(1,100)#spawn a random n
    u = ceil(n**(0.5))
    for i in range(2,u+1):#reduce the testing domain 
        if n%i == 0:
            p=False    #if n has factors, spawn another n


     
print(n)
