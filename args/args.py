#1
def area(a, b=1):    # Non-default and Default parameters respectively. Default parameters cannot be before Non-default parameters
    return a*b
print(area(3,b =4))    # Non-keyword and Keyword parameters respectively

#2
def mean(*args):    # Arbitrary number of Non-keyword Arguments
    return sum(args)/len(args)

print(mean(1,3,5))

#2
def sort_upper(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(sort_upper("snow", "glacier", "iceberg"))

#3
def find_sum(**kwargs):     # Arbitrary number of keyword Arguments
    return sum(kwargs.values())

print(find_sum(a=1,b=2,c=3,d=3))