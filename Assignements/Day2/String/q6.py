stg = input("Enter a sentence: ")
words = stg.split()
reversed_sentence = ' '.join(words[::-1])
print("Reversed sentence:", reversed_sentence)