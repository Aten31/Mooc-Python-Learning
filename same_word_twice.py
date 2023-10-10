# Write your solution here
my_list=[]
word = input("Word:")
my_list.append(word)
i = 0
j=1
while True:
    word = input("Word:")
    if word in my_list:
        break
    else:
        my_list.append(word)
        j+=1
print(f"You typed in {j} different words")

    