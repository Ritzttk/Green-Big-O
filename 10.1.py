class Fraction:
    def __init__(self,x=0,y=0):
        self.nu = x
        self.de = y

    def __str__(self):
        return str(self.nu)+' '+str(self.de)

    def input(self):
        self.nu,self.de = map(int,input().split())

    def ucln(self):
        for i in range(self.de,0,-1):
            if(self.nu%i==0 and self.de%i==0):
                return i


    def simplyfi(self):
        i = self.ucln()
        self.de=self.de//i
        self.nu=self.nu//i

    def sum(self,p2):
        ans=Fraction()
        ans.nu = self.nu * p2.de + p2.nu * self.de
        ans.de = self.de * p2.de
        ans.simplyfi()
        return ans

a=Fraction()
a.input()
b=Fraction()
b.input()

print(a.sum(b))



