mylist = []

num = int(input("Enter a number: "))
mylist.append(num)
stg = str(input("Enter a string: "))
mylist.append(stg)
dec = float(input("Enter a decimal number: "))
mylist.append(dec)
bolen = bool(input("Is this a bolen? (Y/N): "))
mylist.append(bolen)
char = input("Enter only one character: ")
mylist.append(char)

print(mylist[:])
print(mylist[::-1])
