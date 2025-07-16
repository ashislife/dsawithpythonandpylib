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
        if new_node1==None:
            head=new_node1
        else:
            new_node1.next=self.head
            self.head=new_node1
    def traverse(self):
        temp=self.head

        if self.head==None:
            print("LL is empty")
        else:
            while temp!=None:
                temp=temp.next
            temp.next=self.new_node1





