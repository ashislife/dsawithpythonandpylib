class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stackusingLL:
    def __init__(self):
        self.top=None

    def push(self):
        data = int(input("Enter the data for insertition :"))
        new_node=Node (data)
        if self.top==None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
    def pop(self):
        if self.top==None:
            print("Stack does not exits !!")

        else:
            self.top=self.top.next

    def display(self):
        temp=self.top
        while temp:
            print(temp.data)
            temp=temp.next

if __name__=="__main__":
    S=stackusingLL()
    while True:
        print("press1 to push")
        print("press2 to pop")
        print("press3 to display")
        ch=int(input("Enter your choice :"))

        if ch==1:
            S.push()
        elif ch==2:
            S.pop()
        elif ch==3:
            S.display()
        else:
            print("Exit")
            break









