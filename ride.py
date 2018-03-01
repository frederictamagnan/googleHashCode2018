class Ride:
    def __init__(self,liste_ride,index):
        self.a=liste_ride[0]
        self.b=liste_ride[1]
        self.x=liste_ride[2]
        self.y = liste_ride[3]
        self.s = liste_ride[4]
        self.f = liste_ride[5]
        self.index=index


    def __repr__(self):
        return str(self.a)+" "+str(self.b)+" "+str(self.x)+" "+str(self.y)+" "+ str(self.s)+ " "+str(self.f)+" "+str(self.index)