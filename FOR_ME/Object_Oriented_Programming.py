# class MyFirstClass:
#     pass
# object1 = MyFirstClass()
# print(type(object1))
# class Car:
#     def __init__(self,model,name,year,color):
#         self.model = model
#         self.name = name
#         self.year = year
#         self.color = color
# mazda = Car("Mazda","CX-5",2020,"Red")

# class BlogPost:
#     def __init__(self,user_name,text,number_of_likes):
#         self.user_name = user_name
#         self.text = text
#         self.number_of_likes = number_of_likes
# post1 = BlogPost("John","Hello World!",100)
# post2 = BlogPost("Mike","Hello World!",200)
#
# print(post1.number_of_likes)
# print(post2.number_of_likes)

# class Car:
#     wheels_number = 4
#
#     def __init__(self,model,year,color):
#         self.model = model
#         self.year = year
#         self.color = color
#     def info(self):
#         print(f"Машина {self.model} {self.year} года выпуска, имеет цвет {self.color}")
#
# mazda = Car("Mazda",2020,"Red")
#
# mazda.info()
#
# print(t"ddsdsd{mazda.model}")

# class Circle:
#     pi = 3.14
#
#     def __init__(self,radius=1):
#         self.radius = radius
#     def area(self):
#         return self.pi * self.radius ** 2
#
# circle_1 = Circle()
# print(circle_1.area())
# circle_2 = Circle(2)
# print(circle_2.area())

# class GamersForDota:
#
#     Active_players = 0
#
#     def __init__(self, name, age, point):
#         self.name = name
#         self.age = age
#         self.point = point
#         GamersForDota.Active_players += 1
#     def info(self):
#         print(self.name)
#         print(self.age)
#         print(self.point)
#     @classmethod
#     def info_active_players(cls):
#         print(f"Active players: {cls.Active_players}")
# GamersForDota.info_active_players()
# Gamer_1 = GamersForDota("John", 25, 1000)
# Gamer_2 = GamersForDota("Mike", 30, 2000)
# GamersForDota.info_active_players()

class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Parent class initialized")
    def info(self):
        print(self.name)
        print(self.age)

class Kids(Parent):
    def __init__(self, name, age, point):
        super().__init__(name, age)
        self.point = point
        print("Kids class initialized")
    def info(self):
        print(self.name)
        print(self.age)
Kids_1 = Kids("John", 25, 1000)

