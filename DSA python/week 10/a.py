size = 10
table = [[] for i in range(size)]

def insert(key):
    index = key % size
    table[index].append(key)

def display():
    for i in range(size):
        print(i, ":", table[i])

n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

print("Hash Table:")
display()
