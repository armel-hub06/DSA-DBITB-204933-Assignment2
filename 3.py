def find_min(my_list):
    if len(my_list) == 0:
        return None
    min_value = my_list[0]
    for item in my_list[1:]:
        if item < min_value:
            min_value = item
    return min_value
items = input("Enter Your List: ")
my_list = []
for item in items.split():
    my_list.append(int(item))

print(find_min(my_list))