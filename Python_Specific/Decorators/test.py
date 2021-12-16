def smart_multiply(func):
    
    def inner(a,b):
        if(a<0 or b<0):
            a =abs(a)
            b = abs(b)
        return func(a,b)
    return inner

@smart_multiply
def multiply(a,b):
    return a*b 



# multiply = smart_multiply(multiply)

print(multiply(3,-2))
