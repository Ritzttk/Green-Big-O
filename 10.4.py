

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

    def chuvi(self,b,c):
        V=self.khoangcach(b)+self.khoangcach(c)+b.khoangcach(c)
        return V

    def dientich(self,b,c):
        S=((b.tung-self.tung)*(c.hoanh-self.hoanh)-(c.tung-self.tung)*(b.hoanh-self.hoanh))/2
        return S
    def area(self,b,c):
        a=self.khoangcach(b)
        b=self.khoangcach(c)
        c=self.khoangcach(c)
        p=(a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))

    def trongtam(self,b,c):
        ans=diem()
        ans.tung=(self.tung + b.tung +c.tung)/3
        ans.hoanh=(self.hoanh + b.hoanh + c.hoanh)/3
        return ans

a=diem()
a.input()
b=diem()
b.input()
c=diem()
c.input()
print("{0:.2f}".format(a.chuvi(b,c)))
print("{0:.2f}".format(a.area(b,c)))
print("{0:.2f} {1:.2f}".format(a.trongtam(b,c).tung,a.trongtam(b,c).hoanh))









