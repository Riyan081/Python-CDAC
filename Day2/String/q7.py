def pang(sent):
    sent = sent.lower()
    a = set('abcdefghijklmnopqrstuvwxyz')
    return a.issubset(set(sent))

b = input("Enter a sentence: ")

if pang(b):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")