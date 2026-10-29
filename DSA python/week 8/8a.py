
tree = []

def insert(value, i=0):
    global tree

    if i >= len(tree):
        tree.extend([None] * (i - len(tree) + 1))

    if tree[i] is None:
        tree[i] = value
    elif value < tree[i]:
        insert(value, 2 * i + 1)
    elif value > tree[i]:
        insert(value, 2 * i + 2)
    else:
        print("Duplicate values are not allowed.")


def search(value, i=0):
    if i >= len(tree) or tree[i] is None:
        return False

    if tree[i] == value:
        return True
    elif value < tree[i]:
        return search(value, 2 * i + 1)
    else:
        return search(value, 2 * i + 2)


def minimum(i):
    while 2 * i + 1 < len(tree) and tree[2 * i + 1] is not None:
        i = 2 * i + 1
    return i


def delete(value, i=0):
    if i >= len(tree) or tree[i] is None:
        return

    if value < tree[i]:
        delete(value, 2 * i + 1)
    elif value > tree[i]:
        delete(value, 2 * i + 2)
    else:
        left = 2 * i + 1
        right = 2 * i + 2

        has_left = left < len(tree) and tree[left] is not None
        has_right = right < len(tree) and tree[right] is not None

        if not has_left and not has_right:
            tree[i] = None

        elif not has_left:
            tree[i] = tree[right]
            delete_subtree(right, i)

        elif not has_right:
            tree[i] = tree[left]
            delete_subtree(left, i)

        else:
            j = minimum(right)
            tree[i] = tree[j]
            delete(tree[j], right)


def delete_subtree(child, parent):
    if child >= len(tree) or tree[child] is None:
        return

    value = tree[child]
    delete(value, child)

    remaining = collect_subtree(child)
    for v in remaining:
        insert(v)


def collect_subtree(i):
    if i >= len(tree) or tree[i] is None:
        return []

    value = tree[i]
    left = collect_subtree(2 * i + 1)
    right = collect_subtree(2 * i + 2)
    tree[i] = None

    return left + [value] + right


def inorder(i=0):
    if i < len(tree) and tree[i] is not None:
        inorder(2 * i + 1)
        print(tree[i], end=" ")
        inorder(2 * i + 2)


def preorder(i=0):
    if i < len(tree) and tree[i] is not None:
        print(tree[i], end=" ")
        preorder(2 * i + 1)
        preorder(2 * i + 2)


def postorder(i=0):
    if i < len(tree) and tree[i] is not None:
        postorder(2 * i + 1)
        postorder(2 * i + 2)
        print(tree[i], end=" ")


while True:
    print("\n\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display Array")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        insert(value)

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        if search(value):
            delete(value)
            print("Value deleted.")
        else:
            print("Value not found.")

    elif choice == 3:
        value = int(input("Enter value to search: "))
        print("Found" if search(value) else "Not found")

    elif choice == 4:
        inorder()
        print()

    elif choice == 5:
        preorder()
        print()

    elif choice == 6:
        postorder()
        print()

    elif choice == 7:
        print(tree)

    elif choice == 8:
        break

    else:
        print("Invalid choice.")
