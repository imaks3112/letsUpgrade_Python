import math

class cone():
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height

    def Volume(self):
         
        vol = math.pi * (self.Radius * self.Radius) * (self.Height / 3)

        print("Volume of cone: ",vol)

    def Surface_area(self):
        side = math.pi * self.Radius * math.sqrt(self.Radius*self.Radius + self.Height*self.Height)

        print("\n Side of surface area ",side)

        base = math.pi * (self.Radius * self.Radius)    

        print("\n base of surface area ",base)


obj = cone(5,12)
obj.Volume()
obj.Surface_area()


