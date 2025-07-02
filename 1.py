def sum_of_elements(my_list):
    total = 0
    for item in my_list:
        total += item
    return total
items = input("Enter Your List: ")
my_list = []
for item in items.split():
    my_list.append(int(item))

print(sum_of_elements(my_list))