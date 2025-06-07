
mylist = []
name1 = input( " Enter your name: ")
mylist.append(name1)
num1 = (float(input("Enter a decimal value: ")))
mylist.append(num1)
name2 = input ("Enter name: ")
mylist.insert(2, name2)
num2 = int(input("Enter a number: "))
mylist.append(num2)

print(mylist)