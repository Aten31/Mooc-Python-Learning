def first_word(word):
    a = word.find(" ")
    return word[0:(a)]

def second_word(word):
    a = 0
    a = word.find(" ")
    word= word[a+1:]
    a = word.find(" ")
    if a == -1:
        return word[0:]
    else:
        return word[0:a]

def last_word(word):
    i = 1
    while i <= len(word):
        if word[-i] == " ":
            break
        else:
            i+=1
    return(word[-i+1:])    
    
if __name__ == "__main__":
    sentence = "Hello everyone"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))