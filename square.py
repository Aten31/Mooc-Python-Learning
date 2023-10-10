# Copy here code of line function from previous exercise
def line(times,word):
    if word == "":
        print("*"*times)
    else:
        print(word[0]*times)
def square(size,char):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(size, char)
        i += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5,"*")
