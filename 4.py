def has_duplicates(my_list):
    for item1 in range(len(my_list)):
        for item2 in range(item1 + 1, len(my_list)):
            if my_list[item1] == my_list[item2]:
                return True
    return False
items = input("Enter Your List: ")
my_list = []
for item in items.split():
    my_list.append(int(item))
print(has_duplicates(my_list))