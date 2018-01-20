import csv
import math
import random
import matlab.engine

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


hyg=0
ra=[]
dec=[]
distance=[]
def rn():
    #Random number generator
    for i in range(10000):
        ra.append(random.uniform(0,24))
        dec.append(random.uniform(0,180)-90)
        distance.append(random.uniform(200,300))

    
def proper(IPT):
    with open(str(IPT)+".csv") as ipt:
        readcsv=csv.reader(ipt,delimiter=',')
        for row in readcsv:
            ra.append(float(row[0]))
            if hyg==0:
                dec.append(float(row[1])-90.0)
            else:
                dec.append(float(row[1]))
            distance.append(float(row[2]))

response=0

response=input("Type the mode (1:random, 2:data):")

if response==1:
    rn()
elif response==2:
    fname=str(raw_input("Type the file name:"))
    if fname=="hyg":
        hyg=1
        print("HYG database")
    proper(fname)

print("Recording points...")

x=[]
y=[]
z=[]

for i in range(len(ra)):
    x.append((distance[i]*math.cos(math.radians(dec[i])))*math.cos(math.radians(ra[i]*15)))
    y.append((distance[i]*math.cos(math.radians(dec[i])))*math.sin(math.radians(ra[i]*15)))
    z.append(distance[i]*math.sin(math.radians(dec[i])))

print("Plotting starts..")




eng=matlab.engine.start_matlab()
x=matlab.double(x)
y=matlab.double(y)
z=matlab.double(z)

eng.scatter3(x,y,z,1,'filled')

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

ax.scatter(x,y,z,s=0.1)

plt.show()
print("Plotting finished.")

