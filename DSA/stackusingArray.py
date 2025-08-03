class stack:
    def __init__(self):
        self.top = -1
        self.n = 10
        self.arr = [0] * self.n
    def push(self):
        if self.top==self.n-1:
            print("Overflow")

        else:
            data=int(input("Enter the data"))
            self.top=self.top+1
            self.arr[self.top]=data
            print("Item inserted!!!!")

    def pop(self):
        if self.top==-1:
            print("Underflow")
        else:
            self.top=self.top-1
            print("item deleted")
    def display(self):
        print("items are: ")
        for i in range(self.top,-1,-1):
            print(self.arr[i])


if __name__=="__main__":
    S=stack()

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













