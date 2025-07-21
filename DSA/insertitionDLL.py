class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class DoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertitionDLL(self):
        while True:
            data=int(input("Enter the value  :"))
            new_node = Node(data)

            if self.head==None:
                self.head=new_node
                self.tail=new_node

            else:
                print("press 1. insert at beg , 2. insert at end , 3.insert at any pos ")

                m = int(input("Enter your choice: "))

                # at beg
                if m == 1:
                    new_node.next=self.head
                    self.head.prev=new_node
                    self.head=new_node

                # at end
                elif m == 2:
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node

                # at specific pos
                elif m == 3:
                    pos = int(input("Enter the position :"))
                    temp = self.head
                    ptr = temp.next

                    for _ in range(pos - 2):
                        temp = ptr
                        ptr = ptr.next

                    new_node.prev = temp
                    new_node.next = ptr
                    temp.next=new_node
                    ptr.prev = new_node

            ch = int(input("if uhh want to continue pls press 1"))
            if ch != 1:
                break



    def traverse(self):
        if self.head==None:
            print("DLL does not exists ")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data)
                temp=temp.next

if __name__=="__main__":
    dll=DoublyLL()
    dll.insertitionDLL()
    dll.traverse()



















