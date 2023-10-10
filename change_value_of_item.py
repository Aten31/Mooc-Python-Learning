# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
    # Assuming the index is always in the range of the list
    index = int(input("Index: "))
    if index == -1:
        break
    else:
        value = int(input("Value: "))
        my_list[index] = value 
        print(my_list)
