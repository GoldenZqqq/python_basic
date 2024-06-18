# 多态
class Animal(object):
    def speak(self):
        print("Animal speaking")


class Cat(Animal):
    def speak(self):
        print("Meow!")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Test(object):
    def speak(self):
        print("Test!")


def speak(object):  # animal
    object.speak()


animal = Animal()
kitty = Cat()
puppy = Dog()
t = Test()
speak(animal)
speak(kitty)
speak(puppy)
speak(t)
