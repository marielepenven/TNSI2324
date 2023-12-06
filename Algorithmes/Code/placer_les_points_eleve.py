import matplotlib.pyplot as plt
import csv

def ouvrirdoc(mondoc="iris.csv"):
    """ récupére les informations du document csv
    retourne un tableau constitué de dictionnaires"""
   pass
   
   
   
   
   
   

def iris_setosa(tableau):
    iris_set = [(t['petal_length'],t['petal_width']) for t in tableau if t['species']=='0']
    return iris_set

def iris_versicolor(tableau):
    pass
    

def iris_virginica(tableau):
    pass
    
    
    
plt.axis("auto")

lesiris=ouvrirdoc()
iris_seto=iris_setosa(lesiris)
x = []
y=[]
for i in range(len(iris_seto)):
    x.append(float(iris_seto[i][0]))
    y.append(float(iris_seto[i][1]))
plt.plot(x,y,"o",color="red",lw=2,label="iris setosa")








plt.legend()
plt.show()
plt.close()

