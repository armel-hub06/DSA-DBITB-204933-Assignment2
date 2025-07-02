def find_max(my_list):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for item in my_list[1:]:
        if item > max_value:
            max_value = item
    return max_value
items = input("Enter Your List: ")
my_list = []
for item in items.split():
    my_list.append(int(item))

print(find_max(my_list))