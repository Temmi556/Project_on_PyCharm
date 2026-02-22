### LEGB - Local, Enclosing, Global, Built-in
#Local - Локальная область видимости
def gog():
    a_1 = 10 # Локальная область видимости (Local)
    print(a_1)
#Enclosing - Вложенная область видимости
a_2 = 25
def gog_1():
    a_2 = 20
    def gog_2():
        nonlocal a_2
        print(a_2)
    gog_2()
gog_1()
print(a_2)

x = 100
def func():
    global x
    print(x)
    x = 50
    print(x)
func()