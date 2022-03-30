# Add extra features to the function without changing its code.
# In this case we are adding extra features to div function without changing it.




def smart_div(func):
    
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

@smart_div
def div(a,b):
    print(a/b)

# div1 = smart_div(div)
# or 
# div = smart_div(div) # passing parameter


div(2,4) # calling div only
