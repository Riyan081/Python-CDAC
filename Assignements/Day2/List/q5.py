mylist = []
print("Enter 5 numbers: " ,end=' ')
for i in range(5):
    num = int(input())
    mylist.append(num)

print(mylist)

num = int(input("Enter a number to remove: "))
mylist.remove(num)

print(mylist)
