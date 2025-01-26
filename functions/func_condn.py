def convert(value):
    if isinstance(value, dict):
        conversion = sum(value.values()) / len(value)
    else:
        conversion = sum(value) / len(value)
    return conversion

weekday = [37, 38, 39, 40, 41]
weekend = {'saturday': 42, 'sunday': 43}
print(convert(weekend))

#2
def foo(x, array):
    if x in array:
        return True
    else:
        return False

print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))