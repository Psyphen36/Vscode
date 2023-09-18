# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())



# Define the Animal interface
class Animal:
    def make_sound(self):
        return 'motherfucker 69 ' 

# Implement the Dog class following the Animal interface
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Implement the Cat class following the Animal interface
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# Main program
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    # Using the Animal interface to make sounds
    print("Dog says:", dog.make_sound())
    print("Cat says:", cat.make_sound())
