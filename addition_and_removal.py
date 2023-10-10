# Write your solution here
my_list = []
i = 1
while True:
    print("The list is now",my_list)
    task = input("a(d)d, (r)emove or e(x)it:")
    if task == "d":
        my_list.append(i)
        i+= 1
    elif task == "r":
        my_list.pop(-1)
        i-=1
    elif task == "x":
        print("Bye!")
        break