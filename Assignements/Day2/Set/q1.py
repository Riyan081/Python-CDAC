myset = set()
print("Enter 10 values:")

for i in range(10):
    num = input(f"Enter {i+1} value: ")
    myset.add(num)

print("Initial Set:", myset)

remove = input("Enter one more value to remove if present: ")

myset.discard(remove)

print("Updated Set:", myset)