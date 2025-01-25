my_file = open('txt_fl/fruits.txt')
content = my_file.read()
my_file.close()
print(content)

#2
with open('txt_fl/fruits.txt', 'r') as my_file:
    content = my_file.read()

print(content)

#3
def foo(char, filepath='txt_fl/fruits.txt'):
    with open(filepath) as file:
        content = file.read()
    return content.count(char)