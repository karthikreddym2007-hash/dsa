
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    else:
        print("Duplicate values are not allowed.")

    return root


def search(root, value):
    if root is None:
        return False

    if root.data == value:
        return True
    elif value < root.data:
        return search(root.left, value)
    else:
        return search(root.right, value)


def find_min(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, value):
    if root is None:
        return None

    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

while True:
    print("\n\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        root = insert(root, value)

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        if search(root, value):
            root = delete(root, value)
            print("Value deleted.")
        else:
            print("Value not found.")

    elif choice == 3:
        value = int(input("Enter value to search: "))
        if search(root, value):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == 4:
        inorder(root)
        print()

    elif choice == 5:
        preorder(root)
        print()

    elif choice == 6:
        postorder(root)
        print()

    elif choice == 7:
        break

    else:
        print("Invalid choice.")
