def mean(nums):
    my_nums = sum(nums)/len(nums)
    return my_nums

print(f'The mean of the given nums is ',mean([1, 4, 7, 10]))

def convert(amount):
    output = amount * 83.5
    return output
user_input = float(input('Enter a value: '))    #user input
print(convert(user_input))

#string formatting

name = input('Enter your name: ')
size = input('Enter your size: ')

message = f"Hello {name}. {size} is really nice"

print(message)