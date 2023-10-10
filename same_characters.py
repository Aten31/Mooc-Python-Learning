def same_chars(word,index_1,index_2):
    
    if index_1 > (len(word)-1) or index_2 > (len(word)-1):
        return False

    elif word[index_1]==word[index_2]:
        return True
    
    else:
        return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 10))