# Write your solution here
my_list =[]

loop = int(input("How many items:"))
i = 1

while i <= loop:
    item = int(input(f"item i:"))
    my_list.append(item)
    i+= 1

print(my_list)