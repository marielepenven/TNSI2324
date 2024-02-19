from random import *
from tris import *
from timeit import default_timer as timer
import matplotlib.pyplot as plt 

x=[absc for absc in range(0,1001,100)]

y=[]

for i in range(1,1002,100):
    a = timer()
    maliste2=tri_insertion([ randint(0,10000) for k in range(i)])
    b=timer()
    y.append(b-a)

z=[]

t=[]

    
plt.plot(x,y,":",color="red",lw=2,label="tri_insertion")

plt.title("cout des tris")
plt.legend()
plt.show()