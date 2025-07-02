def linear_search(my_list, target):
    for item in range(len(my_list)):
        if my_list[item] == target:
            return item
    return -1

items = input("Enter your list: ")
my_list = []
for item in items.split():
    my_list.append(int(item))

target = int(input("Enter the number to search for: "))
print(linear_search(my_list, target))