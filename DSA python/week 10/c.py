size = 10
table = [-1] * size

def insert(key):
    index = key % size
    i = 0

    while table[(index + i*i) % size] != -1:
        i += 1

    table[(index + i*i) % size] = key

def display():
    for i in range(size):
        print(i, ":", table[i])

n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

print("Hash Table:")
display()
