# Write your solution here
def mean(list):
    i = 0
    sum = 0
    while i<len(list):
        sum += list[i]
        i+=1
    return sum/ len(list)
    



#n test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, 5]
    result = mean(my_list)
    print(result)