
# HASHING USING ARRAY

size = 10

def chaining(keys):
    table = [[] for i in range(size)]

    for key in keys:
        table[key % size].append(key)

    print("Separate Chaining:")
    for i in range(size):
        print(i, ":", table[i])

def linear(keys):
    table = [-1] * size

    for key in keys:
        index = key % size
        count = 0

        while table[index] != -1 and count < size:
            index = (index + 1) % size
            count += 1

        if count < size:
            table[index] = key
        else:
            print("Table full:", key)

    print("Linear Probing:")
    for i in range(size):
        print(i, ":", table[i])

def quadratic(keys):
    table = [-1] * size

    for key in keys:
        index = key % size
        inserted = False

        for i in range(size):
            pos = (index + i*i) % size

            if table[pos] == -1:
                table[pos] = key
                inserted = True
                break

        if not inserted:
            print("Could not insert:", key)

    print("Quadratic Probing:")
    for i in range(size):
        print(i, ":", table[i])

n = int(input("Enter number of elements: "))
keys = []

for i in range(n):
    keys.append(int(input("Enter key: ")))

print("1. Separate Chaining")
print("2. Linear Probing")
print("3. Quadratic Probing")

ch = int(input("Enter choice: "))

if ch == 1:
    chaining(keys)
elif ch == 2:
    linear(keys)
elif ch == 3:
    quadratic(keys)
else:
    print("Invalid choice")
