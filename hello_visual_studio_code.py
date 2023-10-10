# Write your solution here

while True:
    Editor = input("Editor: ")
    Editor = Editor.lower()
    if Editor == "visual studio code":
        print("an excellent choice!")  
        break
    elif Editor == "notepad" or Editor == "word":
        print("awful")
    else:
        print("not good")
    