def insert_begin(self,data):
    new = Node(data)
    ne.next=self.head

def insert_end(self,data):
    new=Node(data)
    if self.head is None:
        self.head=new
    else:
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new

def insertion(slef,index,data):
    if index==0:
        self.insert_begin(data)
        return
    elif index
