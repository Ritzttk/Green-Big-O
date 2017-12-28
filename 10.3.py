import math
class diem:
    def __init__(self,x=0,y=0):
        self.tung=x
        self.hoanh=y

    def input(self):
        self.tung,self.hoanh=map(int,input().split())

    def khoangcach(self,b):
        l = math.sqrt(pow((self.tung-b.tung),2)+pow((self.hoanh-b.hoanh),2))
        return l

a=diem()
a.input()
b=diem()
b.input()
print("{0:.2f}".format(a.khoangcach(b)))


