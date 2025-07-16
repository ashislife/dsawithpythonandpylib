class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None

    def traverse(self):
        if self.head is None:
            print("LL is Empty")
        else:
            temp = self.head

            if self.head is None:
                print("Empty LL")

            while temp:
                print(temp.data)
                temp = temp.next





obj=SingleLinkedList()
n1=Node(10)
obj.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
obj.traverse()




