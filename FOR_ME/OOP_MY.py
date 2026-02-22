class Swimmable:
    def swim(self):
        print(f"{self.name} is swimming")


class Walkable:
    def walk(self):
        print(f"{self.name} is walking")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying")


class Person(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"I am {self.name}")


person = Person("John")

person.speak()
person.swim()
person.walk()
person.fly()
