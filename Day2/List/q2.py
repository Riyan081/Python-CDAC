mylist =[]
while(True):
    num = int(input("Enter a number: "))
    if num==0:
        break
    else:
        mylist.append(num)
print(mylist)
print(len(mylist))