# Ex 1
def cat_voice():
    return print("'Meow!'")
def dog_voice():
    return print("'Woof!'")
cat_voice()
dog_voice()

# Ex 2
def cat_voice():
    return print("'Meow!'"*2)
def dog_voice():
    return print("'Woof!'"*2)
cat_voice()
dog_voice()

# Ex 3
def get_voice(say):
    return print(say+"!")
get_voice("Hello World")

# Ex 4
def generation_not_chestnut_chisel(a, b):
    """
        This function generates a list of odd numbers between a and b (inclusive).
    :param a:
    :param b:
    :return:
    """
    return [x for x in range(a,b+1) if x%2!=0]
print(generation_not_chestnut_chisel(1, 10))


