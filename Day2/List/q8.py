mylist = []
for i in range(1, 21):
    mylist.append(i)

print(mylist)

oddlist = [i for i in mylist if i % 2 != 0]
print(oddlist)