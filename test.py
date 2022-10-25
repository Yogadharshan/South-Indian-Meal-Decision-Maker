import random
from string import printable
list = ["Lambo","asdf","asdf4w"]
print(list[0])
print(type(random.randint(0,len(list)-1)))
b = list[random.randint(0,len(list - 1))]
def random_element(x):
    a = random.randint(0,len(x-1))
    return a
b = list(random_element(list))
print (b)