class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class singleLinkedList:
    def __init__(self):
        # head ko globally or object dono me use krna hai esliye self. lagega warna locally kaam rhta to simple head=None hota
        self.head = None

    # insert beg of the LL
    def insertatbeg(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def traverse(self):
        temp = self.head

        if self.head == None:
            print("LL does not exit ")
        else:
            while (temp != None):
                print(temp.data)
                temp = temp.next

obj=singleLinkedList()
n1=Node(10)
obj.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3

obj.traverse()













