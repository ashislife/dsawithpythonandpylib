class Node :
    def __init__(self, data):
        self.data=data
        self.next=None


class insertitionSLLend:
    def __init__(self):
        self.head=None


    def insertatend(self,data):
        new_node1=Node(data)

        # use for node connection if exist
        if self.head==None:
            self.head=new_node1
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=new_node1

    def display(self):
        if self.head==None:
            print("LL does not exists")
        else:
            temp=self.head
            while (temp!=None):
                print(temp.data)
                temp=temp.next

if __name__=="__main__":
     linklist = insertitionSLLend()

     while True:
         print("\n insert to end ")
         print("\n Display")
         print("\n Exit ")
         choice = int(input("Enter your choice..."))

         if choice == 1:
             data = int(input("Enter data to insert"))
             linklist.insertatend(data)
         elif choice == 2:
             linklist.display()

         elif choice == 3:
             print("Exit")

         else:
             print("This is invalid choice !!!!!")



















