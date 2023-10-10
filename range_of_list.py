# Write your solution here
def range_of_list(list):
    low,high = list[0],list[0]
    for number in list:
        if number>high:
            high = number
        if number<low:
            low = number
    
    return (high-low)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 3, 67, 7, 4, 23, 1, 5, 7, 4]
    result = range_of_list(my_list)
    print(result)