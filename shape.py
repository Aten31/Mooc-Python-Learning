def line(times,word):
    if word == "":
        print("*"*times)
    else:
        print(word[0]*times)


def shape(height,triangle_var,length,rect_var):
    i,j = 1,1
    while i <= height:
        line(i, triangle_var)
        i += 1
    while j <= length:
        line(height,rect_var)
        j += 1

if __name__ == "__main__":
    shape(5, "X", 3, "*")

 