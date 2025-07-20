class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class creationLL:


    def __init__(self):
        self.head = None

    def insertitionLL(self):
        while True:
            data = int(input("Enter the value : "))
            new_node = Node(data)

            if self.head == None:
                self.head = new_node

            else:
                print("\n press1. insert at beg")
                print("\n press2. insert at end")
                print("\n press3. insert at specific pos")

                m = int(input("Enter your choice :"))

                if m == 1:
                    new_node.next = self.head
                    self.head = new_node
                elif m == 2:
                    temp = self.head
                    while (temp.next != None):
                        temp = temp.next
                    temp.next = new_node

                elif m == 3:
                    pos = int(input("Enter the position: "))
                    temp = self.head
                    for i in range(pos - 2):
                        temp = temp.next
                    new_node.next = temp.next
                    temp.next = new_node
                ch = int(input("If you want to continue press 1"))

                if ch != 1:
                    break






    def traverse(self):
        if self.head == None:
            print("LL does not exists")
        else:
            temp = self.head
            while (temp != None):
                print("inserted value :", temp.data)
                temp = temp.next


if __name__ == "__main__":
    ll = creationLL()
    ll.insertitionLL()
    ll.traverse()


















