

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def __del__(self):
        print(f"Deleting student {self.name}")


s1 = student("Alice", 20)
s2 = student("Bob", 22)

s1 = s2
s1.display()
s2.display()

# Deleting the objects
# del s1
# del s2

# This will call the __del__ method
# Note: The __del__ method is called when the object is about to be destroyed.
# However, it's not guaranteed to be called immediately after the del statement.
# It's better to use context managers or explicit cleanup methods for resource management.



def __str__(self):

        return str(self.rollno)


