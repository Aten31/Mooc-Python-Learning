# Write your solution here
my_list = []
i = 1
while True:
    task = int(input("New item:"))
    if task == 0:
        print("Bye!")
        break
    else:
        my_list.append(task)
        print("The list now:",my_list)
        print("The list in order:",sorted(my_list))
