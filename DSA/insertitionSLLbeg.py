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

    def display(self):
        temp = self.head

        if self.head == None:
            print("LL does not exit ")
        else:
            while (temp != None):
                print(temp.data)
                temp = temp.next

if __name__=="__main__":
    linklist=singleLinkedList()
    while True:
        print("\n1. Insert at beg ")
        print("\n2. display ")
        print("\n3. Exit ")
        choice=int(input("Enter your choice :"))

        if choice == 1:
            data=int(input("Enter data to insert"))
            linklist.insertatbeg(data)
        elif choice==2:
            linklist.display()
        elif choice==3:
            print ("Exit program ")
            break
        else:
            print("Invalid choice pls try Again !!!")


















