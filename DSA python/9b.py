
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    return 0 if root is None else root.height


def balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)


def update(root):
    root.height = 1 + max(height(root.left), height(root.right))


def rotate_right(y):
    x = y.left
    t = x.right

    x.right = y
    y.left = t

    update(y)
    update(x)
    return x


def rotate_left(x):
    y = x.right
    t = y.left

    y.left = x
    x.right = t

    update(x)
    update(y)
    return y


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    update(root)
    bf = balance(root)

    if bf > 1 and key < root.left.key:
        return rotate_right(root)

    if bf < -1 and key > root.right.key:
        return rotate_left(root)

    if bf > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if bf < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


def min_node(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = min_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    update(root)
    bf = balance(root)

    if bf > 1 and balance(root.left) >= 0:
        return rotate_right(root)

    if bf > 1 and balance(root.left) < 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if bf < -1 and balance(root.right) <= 0:
        return rotate_left(root)

    if bf < -1 and balance(root.right) > 0:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


def search(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)

    return search(root.right, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")


root = None

while True:
    print("\n\n--- AVL TREE USING LINKED LIST ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        key = int(input("Enter value: "))
        root = insert(root, key)
        print("Node inserted.")

    elif choice == '2':
        key = int(input("Enter value: "))
        if search(root, key):
            root = delete(root, key)
            print("Node deleted.")
        else:
            print("Value not found.")

    elif choice == '3':
        key = int(input("Enter value: "))
        if search(root, key):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == '4':
        inorder(root)
        print()

    elif choice == '5':
        preorder(root)
        print()

    elif choice == '6':
        postorder(root)
        print()

    elif choice == '7':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
