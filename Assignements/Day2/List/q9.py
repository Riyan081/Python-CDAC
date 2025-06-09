mylist = []
print("Enter 5 numbers: " ,end=' ')
for i in range(5):
    num = int(input())
    mylist.append(num)

print(mylist)

mylist.sort()
print("Sorted List (Ascending):", mylist)

mylist.sort(reverse=True)
print("Sorted List (Descending):", mylist)