def smart_add(func):

    def inner(a,b):
        if(a<0 or b<0):
            a = abs(a)
            b = abs(b)
        return func(a,b)
    return inner


@smart_add
def add(a,b):
    return a+b

# add = smart_add(add)


print(add(-13,4))
f = lambda a,b,c,d:a*b*c*d 
print(f(4,2,1,3))