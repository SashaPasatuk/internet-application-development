import random

def gen_random(a,b,c):
    for _ in range(a):
        yield random.randint(b, c)

#print(list(gen_random(5,1,3)))


