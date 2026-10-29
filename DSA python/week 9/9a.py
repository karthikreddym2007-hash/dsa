
keys = []
left = []
right = []
heights = []
root = -1


def new_node(key):
    i = len(keys)
    keys.append(key)
    left.append(-1)
    right.append(-1)
    heights.append(1)
    return i


def height(i):
    return 0 if i == -1 else heights[i]


def update(i):
    heights[i] = 1 + max(height(left[i]), height(right[i]))


def balance(i):
    return 0 if i == -1 else height(left[i]) - height(right[i])


def rotate_right(y):
    x = left[y]
    t = right[x]

    right[x] = y
    left[y] = t

    update(y)
    update(x)
    return x


def rotate_left(x):
    y = right[x]
    t = left[y]

    left[y] = x
    right[x] = t

    update(x)
    update(y)
    return y


def insert(node, key):
    if node == -1:
        return new_node(key)

    if key < keys[node]:
        left[node] = insert(left[node], key)
    elif key > keys[node]:
        right[node] = insert(right[node], key)
    else:
        return node

    update(node)
    bf = balance(node)

    if bf > 1 and key < keys[left[node]]:
        return rotate_right(node)

    if bf < -1 and key > keys[right[node]]:
        return rotate_left(node)

    if bf > 1 and key > keys[left[node]]:
        left[node] = rotate_left(left[node])
        return rotate_right(node)

    if bf < -1 and key < keys[right[node]]:
        right[node] = rotate_right(right[node])
        return rotate_left(node)

    return node


def min_node(node):
    while left[node] != -1:
        node = left[node]
    return node


def delete(node, key):
    if node == -1:
        return -1

    if key < keys[node]:
        left[node] = delete(left[node], key)
    elif key > keys[node]:
        right[node] = delete(right[node], key)
    else:
        if left[node] == -1:
            return right[node]

        if right[node] == -1:
            return left[node]

        temp = min_node(right[node])
        keys[node] = keys[temp]
        right[node] = delete(right[node], keys[temp])

    update(node)
    bf = balance(node)

    if bf > 1 and balance(left[node]) >= 0:
        return rotate_right(node)

    if bf > 1 and balance(left[node]) < 0:
        left[node] = rotate_left(left[node])
        return rotate_right(node)

    if bf < -1 and balance(right[node]) <= 0:
        return rotate_left(node)

    if bf < -1 and balance(right[node]) > 0:
        right[node] = rotate_right(right[node])
        return rotate_left(node)

    return node


def search(node, key):
    while node != -1:
        if keys[node] == key:
            return True

        if key < keys[node]:
            node = left[node]
        else:
            node = right[node]

    return False


def inorder(node):
    if node != -1:
        inorder(left[node])
        print(keys[node], end=" ")
        inorder(right[node])


def preorder(node):
    if node != -1:
        print(keys[node], end=" ")
        preorder(left[node])
        preorder(right[node])


def postorder(node):
    if node != -1:
        postorder(left[node])
        postorder(right[node])
        print(keys[node], end=" ")


while True:
    print("\n\n--- AVL TREE USING ARRAYS ---")
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
        print("Value found." if search(root, key)
              else "Value not found.")

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
        break

    else:
        print("Invalid choice.")
