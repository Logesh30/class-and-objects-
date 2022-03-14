class student:

    def __init__(self,name,phy,che,bio):
        self.name=name
        self.phy=phy
        self.che=che
        self.bio=bio
    def total_marks(self):
        return self.phy+self.che+self.bio
    def percentage(self):
        return (self.total_marks()*100)//300
logesh=student("logesh",90,90,80)

print("total marks obtained by "+ logesh.name,"is",logesh.total_marks())
print("percentage of "+ logesh.name,"is",logesh.percentage())
