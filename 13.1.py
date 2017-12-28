import sys
sys.setrecursionlimit(1000000000)

class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def min(self):
        if(self.left):
            return self.left.min()
        else:
            return self.data


class BST:
    def __init__(self):
        self.root = None

    def add(self,data):
        if(self.root == None):
            p = Node(data)
            self.root = p
        else:
            self.addNode(self.root,data)

    def addNode(self,cur,data):
        if(data < cur.data):
            if(cur.left):
                self.addNode(cur.left, data)
            else:
                cur.left = Node(data)
        if(data > cur.data):
            if(cur.right):
                self.addNode(cur.right,data)
            else:
                cur.right=Node(data)

    def min(self):
        return self.root.min()


T = BST()
n = int(input())
a = map(int,input().split())
for i in a:
    T.add(i)

print(T.min())








