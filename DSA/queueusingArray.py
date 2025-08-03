class QueueDSA:
    def __init__(self):
        self.front=-1
        self.rare=-1
        self.n = 10
        self.queue= [0] * self.n

    def enqueue(self):
        if self.rare==self.n-1:
            print("Queue is an overflow condition!!")

        else:
            data = int(input("Enter the data: "))
            if self.front ==-1 and self.rare==-1:
                self.front=0
                self.rare=0
                self.queue[self.rare]=data
            else:
                self.rare = self.rare + 1
                self.queue[self.rare] = data


    def dequeue(self):
        if self.front ==-1 and self.rare==-1:
            print("Queue in underflow condition !!!")
        else:
            self.front=self.front+1

    def display(self):
        print("Total value :")
        for i in range(self.front,self.rare+1):
            print(self.queue[i])


if __name__=="__main__":
    q=QueueDSA()
    while True:
        print("press1 to Enqueue")
        print("press2 to Dequeue")
        print("press3 to display")
        ch=int(input("Enter your choice :"))

        if ch==1:
            q.enqueue()
        elif ch==2:
            q.dequeue()
        elif ch==3:
            q.display()
        else:
            print("Exit")
            break










