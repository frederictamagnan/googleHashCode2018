import math
class Riders:

    def __init__(self,data):
        self.rides_attributed=[]
        self.step_min=0
        self.x_rider=0
        self.y_rider=0
        self.data=data
    def attribute_ride(self,ride):
        self.rides_attributed.append(ride.index)
        ride = self.data.rides_dict[ride.index]
        self.step_min += abs(ride.x - ride.a) + abs(ride.y - ride.b)
        self.step_min += abs(self.x_rider - ride.a) + abs(self.y_rider - ride.b)


    def output(self):
        list1=[len(self.rides_attributed)]+self.rides_attributed

        str1 = ' '.join(str(e) for e in list1)
        return str1


    def __repr__(self):

        return str(self.rides_attributed)

