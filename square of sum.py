class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sq_sum(self):
        return self.x**2 + self.y**2 + self.z**2


obj1=point(1,3,5)

print(obj1.sq_sum())