a = [1,2,3]
b = [3,4,5]
c = 7

def tuple_unpack(a,b,c):
    return (*a, *b, c)
    
tuple_unpack(a, b, c)
