class Animal:
    pass

class Dog(Animal):
    pass


d=Dog()

print(f"Is d is an instance of Dog? : {bool(isinstance(d,Dog))} ")
print(f"Is d is instance of Animal? : {bool(isinstance(d,Animal))}")
print()
print(f"Is Dog is subclass of Animal? : {bool(issubclass(Dog,Animal))}")
print(f"Is Dog instance of Animal? : {bool(isinstance(Dog,Animal))}")
