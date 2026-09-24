class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of nodes: "))
        self.head = None
        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = new_node
                new_node.next = self.head
        print("Circular Linked List created successfully.")

    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        print(f"Inserted {data} at the end.")

    def insert_at_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        if index < 0:
            print("Invalid index.")
            return
        if index == 0:
            self.insert_beginning()
            return
        if self.head is None:
            print("Index out of range.")
            return
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
            if temp == self.head:
                print("Index out of range.")
                return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {data} at index {index}.")

    def delete_by_value(self):
        value = int(input("Enter value to delete: "))
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        if self.head.data == value:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            print(f"Deleted {value}.")
            return
        temp = self.head
        while temp.next != self.head:
            if temp.next.data == value:
                temp.next = temp.next.next
                print(f"Deleted {value}.")
                return
            temp = temp.next
        print(f"{value} not found in the Linked List.")

    def delete_first(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        deleted = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        print(f"Deleted first node: {deleted}")

    def delete_last(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        if self.head.next == self.head:
            deleted = self.head.data
            self.head = None
            print(f"Deleted last node: {deleted}")
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        deleted = temp.next.data
        temp.next = self.head
        print(f"Deleted last node: {deleted}")

    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return
        count = 0
        temp = self.head
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")

    def display_head_tail(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        print("Head:", self.head.data)
        print("Tail:", temp.data)

    def display_tail_to_head(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        tail = self.head
        while tail.next != self.head:
            tail = tail.next
        print("Data from Tail to Head:", end=" ")
        current = tail
        while True:
            print(current.data, end=" ")
            if current == self.head:
                break
            temp = self.head
            while temp.next != current:
                temp = temp.next
            current = temp
        print()

cll = CircularLinkedList()

while True:
    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display")
    print("10. Display Head and Tail")
    print("11. Print Data from Tail to Head")
    print("12. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()
    elif choice == 2:
        cll.insert_beginning()
    elif choice == 3:
        cll.insert_end()
    elif choice == 4:
        cll.insert_at_index()
    elif choice == 5:
        cll.delete_by_value()
    elif choice == 6:
        cll.delete_first()
    elif choice == 7:
        cll.delete_last()
    elif choice == 8:
        cll.count_nodes()
    elif choice == 9:
        cll.display()
    elif choice == 10:
        cll.display_head_tail()
    elif choice == 11:
        cll.display_tail_to_head()
    elif choice == 12:
        print("Exiting program....")
        break
    else:
        print("Invalid choice. Please try again.")
