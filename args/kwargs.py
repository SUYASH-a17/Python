def mean(**kwargs):
    return kwargs

print(mean(a=1,b=2,c=5))

#2
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=1,b=2,c=3,d=3))