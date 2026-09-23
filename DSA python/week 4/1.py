class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
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
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node
        print("Linked List created successfully.")

    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end.")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at the end.")

    def insert_at_index(self):
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))
        if index < 0:
            print("Invalid index.")
            return
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at index {index}.")
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Index out of range.")
                return
            temp = temp.next
        if temp is None:
            print("Index out of range.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {data} at index {index}.")

    def delete_by_value(self):
        value = int(input("Enter value to delete: "))
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == value:
            self.head = self.head.next
            print(f"Deleted {value}.")
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print(f"Deleted {value}.")
                return
            temp = temp.next
        print("Value not found.")

    def delete_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        deleted_data = self.head.data
        self.head = self.head.next
        print(f"Deleted {deleted_data} from the beginning.")

    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            print(f"Deleted {deleted_data} from the end.")
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        deleted_data = temp.next.data
        temp.next = None
        print(f"Deleted {deleted_data} from the end.")

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

sll = SLL()

while True:
    print("\n----- SINGLY LINKED LIST -----")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sll.create()
    elif choice == 2:
        sll.insert_beginning()
    elif choice == 3:
        sll.insert_end()
    elif choice == 4:
        sll.insert_at_index()
    elif choice == 5:
        sll.delete_by_value()
    elif choice == 6:
        sll.delete_beginning()
    elif choice == 7:
        sll.delete_end()
    elif choice == 8:
        sll.count_nodes()
    elif choice == 9:
        sll.display()
    elif choice == 10:
        print("Exiting from the program...")
        break
    else:
        print("Invalid choice.")
