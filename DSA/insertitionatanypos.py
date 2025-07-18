class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class insertitionLL:
    def __init__(self):
        self.head=None

    def insertAtAnyPos(self,data,pos):
        new_node=Node(data)


        if self.head==None:
            self.head=new_node

        else:
            temp=self.head
            for i in range(pos-2):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node

    def traverse(self):
        if self.head==None:
            print("LL does not exists")
        else:
            temp=self.head
            while(temp!=None):
                print("inserted value :",temp.data)
                temp=temp.next




ll=insertitionLL()

while True:
    data = int(input("Insert value :"))
    pos = int(input("Enter the position :"))

    ll.insertAtAnyPos(data,pos)

    ll.traverse()

    ch = input("Continue? (y/n): ")
    if ch != 'y':
        break








