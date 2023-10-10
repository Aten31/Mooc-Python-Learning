def spruce(num):
    print("a spruce!")
    i = 1
    while i  <= num:
        spruce_logs = ((num-i)*" ")+((2*i-1)*"*")
        print(spruce_logs)
        i += 1
    print(((num-1)*" ")+((2*1-1)*"*"))

if __name__ == "__main__":
    spruce(9)