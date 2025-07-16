class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None


    def display(self):
        if self.head is None:
            print("LL is Empty")



L=SingleLinkedList()
L.display()





