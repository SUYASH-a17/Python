#list
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for items in colors:
    if isinstance(items, int) and items > 50:
        print(items)

#dict
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print(f'{key}: {value}')