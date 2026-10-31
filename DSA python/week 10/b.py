size = 10
table = [-1] * size

def insert(key):
    index = key % size

    while table[index] != -1:
        index = (index + 1) % size

    table[index] = key

def display():
    for i in range(size):
        print(i, ":", table[i])

n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

print("Hash Table:")
display()
