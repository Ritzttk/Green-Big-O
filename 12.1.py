class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setNext(self,new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.headNode=None
        self.tailNode=None

    def insertTail(self,data):
        p = Node(data)

        if(self.headNode == None and  self.tailNode == None):
            self.headNode=self.tailNode=p
        else:
            self.tailNode.setNext(p)
            self.tailNode=p

    def traverse(self):
        cur=self.headNode
        while(cur):
            cur=cur.getNext()

    def min(self):
        if(self.headNode==self.tailNode==None):
            return None
        min=self.headNode
        cur = self.headNode
        while(cur):
            if(cur.getData() < min.getData()):
                min = cur
            cur=cur.getNext()
        return min

    def count_min(self):
        

a= list(map(int,input().split()))
ls = LinkedList()
for e in a:
    if(e!=0):
        ls.insertTail(e)
    else:
        break

ans=ls.min()
if(ans is None):
    print(0)
else:
    print(ans.getData())



