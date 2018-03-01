import csv
from ride import Ride
from riders import Riders
import math
import matplotlib.pyplot as plt
results = []
with open('./datasets/e_high_bonus.in', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row)

results2=[]
for elt in results:
    results2.append(elt[0].split(' '))

results3=[]
for elt in results2:
    results3.append(list(map(int, elt)))

# print(results3)

class Data:

    def __init__(self,input):



        self.R=input[0][0]
        self.C=input[0][1]
        self.F=input[0][2]
        self.N=input[0][3]
        self.B=input[0][4]
        self.T=input[0][5]

        self.rides=[]
        self.rides_dict={}
        for k,v in enumerate(input[1:]):
            self.rides.append(Ride(v,k))
            self.rides_dict[k]=Ride(v,k)

        self.riders=[]

        for i in range(0,self.F):
            self.riders.append(Riders(self))



    def earliest_run(self,reverse):
        self.rides = sorted(self.rides, key=lambda x: x.s, reverse=reverse)




    def __repr__(self):
        strr=""
        strr=str(self.R)+" "+str(self.C)+" "+str(self.F)+" "+str(self.N)+" "+str(self.B)+"\n"
        for i in self.rides:
            strr+=str(i)+"\n"
        return strr


    def method1(self):

        nb_rides_per_rider=len(self.rides)//self.R
        nb_rides_left=len(self.rides)%self.R

        self.earliest_run(reverse=True)
        for ride in self.rides:
            self.riders = sorted(self.riders, key=lambda x: x.step_min, reverse=False)
            for rider in self.riders:
                if self.rides ==[]:
                    return 0
                else:
                    rider.attribute_ride(self.rides.pop())

        print(self.riders)


    def output(self,name):
        thefile = open('./datasets/out/'+name, 'w')
        for rider in self.riders:

            thefile.write("%s\n" % rider.output())


    def distance(self):

        for rider in self.riders:
            rider.distance=0
            for ride_index in rider.rides_attributed:
                ride=self.rides_dict[ride_index]
                rider.distance+=abs(ride.x-ride.a)+abs(ride.y-ride.b)







data=Data(results3)
# print(data1.B)
# print(data1)

# print(data1)

data.method1()
data.distance()
data.output('e_high_bonus.out')

distances=[]




print(data.N)

