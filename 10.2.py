class hocsinh:
    def __init__(self,a=0,b=0,c=0):
        self.ten = a
        self.toan = b
        self.van = c

    def input(self):
        self.ten = input()
        self.toan,self.van = map(float,input().split())

    def dtb(self):
        print(self.ten)
        print("{0:.2f}".format((self.toan+self.van)/2))


a=hocsinh()
a.input()
a.dtb()



