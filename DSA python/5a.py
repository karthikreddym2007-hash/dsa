class StackEx:
    def __init__(self,size):
        self.size=size
        self.stack=[None]*size
        self.top=-1
    def push(self,item):
        if self.top==self.size-1:
            print("Stack overflow")
        else:
            self.top+=1
            self.stack[self.top]=item
            print(item,"pushed into stack")
    def pop(self):
        if self.top==-1:
            print("Stack underflow")
        else:
            item=self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            print(item,"popped from stack")
    def peek(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            print("top element:",self.stack[self.top])
    def display(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print("The elements of the stack are: ")
            for i in range(self.top,-1,-1):
                print(self.stack[i])
size = int(input("Enter the size of the stack: "))
s = StackEx(size)
while True:
    print("\n---- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter the element to push: "))
        s.push(item)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice")
