from random import randint


def function_1(s):
    return[x for x in s if x%2!=0]

a = []
for i in range(1,10):
    a.append(randint(1,1000))
print(function_1(a))

def function_with_kwargs(**kwargs):
    print(kwargs)
function_with_kwargs(a=1,b=2,c=3)