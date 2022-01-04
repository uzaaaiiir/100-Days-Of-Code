def add(*args):
    count = 0
    # lst = list(args)
    # print(lst)
    for item in args: 
        count += item
    return count

print(add(1,2,3,4,5, 10))

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)