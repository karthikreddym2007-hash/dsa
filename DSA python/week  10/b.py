size = 10

class Node:
    def __init__(self, key=-1):
        self.key = key
        self.next = None

def create_table():
    head = Node()
    temp = head
    for i in range(size-1):
        temp.next = Node()
        temp = temp.next
    return head

def get_node(head, index):
    temp = head
    for i in range(index):
        temp = temp.next
    return temp

def chaining(keys):
    table = [None]*size
    for key in keys:
        index = key%size
        newnode = Node(key)
        newnode.next = table[index]
        table[index] = newnode
    print("Separate Chaining:")
    for i in range(size):
        print(i,":",end=" ")
        temp = table[i]
        while temp:
            print(temp.key,end=" -> ")
            temp = temp.next
        print("None")

def linear(keys):
    head = create_table()
    for key in keys:
        index = key%size
        count = 0
        while get_node(head,index).key!=-1 and count<size:
            index = (index+1)%size
            count+=1
        if count<size:
            get_node(head,index).key = key
        else:
            print("Table Full:",key)
    print("Linear Probing:")
    for i in range(size):
        print(i,":",get_node(head,i).key)

def quadratic(keys):
    head = create_table()
    for key in keys:
        index = key%size
        inserted = False
        for i in range(size):
            pos = (index+i*i)%size
            if get_node(head,pos).key==-1:
                get_node(head,pos).key = key
                inserted = True
                break
        if not inserted:
            print("Could not insert:",key)
    print("Quadratic Probing:")
    for i in range(size):
        print(i,":",get_node(head,i).key)

n = int(input("Enter number of elements: "))
keys = []
for i in range(n):
    keys.append(int(input("Enter key: ")))
print("1. Separate Chaining")
print("2. Linear Probing")
print("3. Quadratic Probing")
ch = int(input("Enter choice: "))
if ch==1:
    chaining(keys)
elif ch==2:
    linear(keys)
elif ch==3:
    quadratic(keys)
else:
    print("Invalid Choice")
