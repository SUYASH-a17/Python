with open('txt_fl/vegetables.txt', 'w') as my_file:
    my_file.write('Tomato')

#2
with open('txt_fl/bear.txt','r') as char:
    content = char.read()

with open('txt_fl/first.txt','w') as char:
    char.write(content[:90])

#3
with open('txt_fl/fruits.txt', 'a+') as my_file:
    my_file.write('\nokra')
    my_file.seek(0)
    my_content = my_file.read()
print(my_content)

#4
with open('txt_fl/fruits.txt','r') as file:
    content = file.read()

with open('txt_fl/first.txt', 'a') as file:
    my_content = file.write(content)

print(my_content)

#5
with open('data.txt','a+') as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content*2)
