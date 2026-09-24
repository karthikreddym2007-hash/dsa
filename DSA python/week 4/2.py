class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        print("Insertion Completed")

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp
        print("Insertion Completed")

    def insert_index(self, index, data):
        if index < 0:
            print("Invalid Index")
        elif index == 0:
            self.insert_begin(data)
        else:
            temp = self.head
            for i in range(index - 1):
                if temp is None:
                    print("Invalid Index")
                    return
                temp = temp.next
            if temp is None:
                print("Invalid Index")
                return
            new = Node(data)
            new.next = temp.next
            new.prev = temp
            if temp.next:
                temp.next.prev = new
            temp.next = new
            print("Insertion Completed")

    def deleteBeg(self):
        if self.head is None:
            print("Can't perform delete operation")
        elif self.head.next is None:
            self.head = None
            print("Value Deleted")
        else:
            self.head.next.prev = None
            self.head = self.head.next
            print("Value Deleted")

    def deleteEnd(self):
        if self.head is None:
            print("Can't perform delete operation")
        elif self.head.next is None:
            self.head = None
            print("Value Deleted")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
            print("Value Deleted")

    def deleteIndex(self, index):
        if self.head is None:
            print("Can't perform delete operation")
        elif index < 0:
            print("Invalid Index")
        elif index == 0:
            self.deleteBeg()
        else:
            temp = self.head
            for i in range(index):
                if temp is None:
                    print("Invalid Index")
                    return
                temp = temp.next
            if temp is None:
                print("Invalid Index")
            elif temp.next:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                print("Value Deleted")
            else:
                temp.prev.next = None
                print("Value Deleted")

    def displayFwd(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def displayBwd(self):
        if self.head is None:
            print("None")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

Dll = DoublyLinkedList()

while True:
    print("\n1.Insert Beginning")
    print("2.Insert End")
    print("3.Insert at Index")
    print("4.Delete at Beginning")
    print("5.Delete at End")
    print("6.Delete at Specific Index")
    print("7.Display Forward")
    print("8.Display Backward")
    print("9.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        x = int(input("Value: "))
        Dll.insert_begin(x)
        Dll.displayFwd()
    elif ch == 2:
        x = int(input("Value: "))
        Dll.insert_end(x)
        Dll.displayFwd()
    elif ch == 3:
        idx = int(input("Index: "))
        x = int(input("Value: "))
        Dll.insert_index(idx, x)
        Dll.displayFwd()
    elif ch == 4:
        Dll.deleteBeg()
        Dll.displayFwd()
    elif ch == 5:
        Dll.deleteEnd()
        Dll.displayFwd()
    elif ch == 6:
        idx = int(input("Index: "))
        Dll.deleteIndex(idx)
        Dll.displayFwd()
    elif ch == 7:
        Dll.displayFwd()
    elif ch == 8:
        Dll.displayBwd()
    elif ch == 9:
        print("Loop Terminated")
        break
    else:
        print("Invalid Choice")
