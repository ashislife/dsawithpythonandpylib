class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class circularLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertitionCLL(self):
        while True:
            data = int(input("Enter the data for insertition :"))
            new_node = Node(data)

            if self.head==None:
                self.head=new_node
                self.tail=new_node
                new_node.next=self.head

            else:
                print("1.insert at beg ,2.insert a end , 3.insert at specific pos : ")

                m=int(input("press the key for insertition "))

                # insert at beg in CLL
                if m==1:
                    new_node.next=self.head
                    self.head=new_node
                    self.tail.next=new_node
                # insert at end in CLL
                elif m==2:
                    self.tail.next=new_node
                    self.tail=new_node
                    new_node.next=self.head


                # insert at any pos in CLL
                elif m==3:
                    pos=int(input("Enter the position if you want to insert :"))
                    temp=self.head
                    for _ in range(pos-2):
                        temp=temp.next

                    new_node.next=temp.next
                    temp.next=new_node
                choice=int(input("if uh want to continue pree 1 :"))
                if choice!=1:
                    break

    def traverse(self):
        if self.head==None:
            print("CLL does not exists")

        else:
            temp=self.head
            while True:
                print("Node:", temp.data)
                temp = temp.next
                if temp == self.head:
                    break

if __name__=="__main__":
    ll=circularLL()
    ll.insertitionCLL()
    ll.traverse()

















