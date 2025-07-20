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

    def delectionCLL(self):
        while True:
            print("press 1. del beg in CLL , 2. del end in CLL , 3. del at specific pos ")
            m = int(input("Enter the position to delete :"))

            if m == 1:
                temp=self.head
                temp=temp.next
                self.head=temp
                self.tail.next=temp

            elif m==2:
                temp=self.head
                ptr=temp.next
                while(ptr.next!=self.head):
                    temp=ptr
                    ptr=ptr.next

                temp.next=self.head
                tail=temp

            elif m==3:
                pos=int(input("Enter the position if uhh want to delete :"))
                temp=self.head
                ptr=temp.next
                for _ in range(pos-2):
                    temp=ptr
                    ptr=ptr.next
                temp.next=ptr.next

            ch=int(input("if uh want to continue press 1 :"))

            if ch!=1:
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
    ll.delectionCLL()
    ll.traverse()

















