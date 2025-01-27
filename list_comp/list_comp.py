#creates a list by iterating over another container.

#1 for loop
squares = [x**2 for x in range(10)]
print(squares)

#2 if condition
def great(num):
    return [i for i in num if i > 0]

print(great([-5, 3, -1, 101]))

#3 if-else condition
def zero(num):
    return[i if isinstance(i, int) else 0 for i in num]

zero([99, 'no data', 95, 94, 'no data'])

#4 nested for loops
cartesian = [(x,y) for x in [1,2,3] for y in [4,5,6]]
print(cartesian)

#5 Flattening a list of list
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened = [item for sublist in list_of_lists for item in sublist]

print(flattened)