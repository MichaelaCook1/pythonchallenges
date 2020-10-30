##best conjugations

def get_all_words():
    with open('wordlist.txt' ,"r") as word_list:  #opens textfile and defines it
        words = []  #defines empty list
        for line in word_list:
            new_line = line[:len(line) - 1] #to move to next word 
            words.append(new_line)          #to append new word within the list
    return words

def best_conjugation(word_1):   
    all_words = get_all_words()            #defines all words in list
    list_of_valid_subwords = []            #to present sub words as a list
    for word in all_words:
        if word_1.find(word) >=0:          #finds sub-words within word in list
            list_of_valid_subwords.append(word)
    msg = f"{len(list_of_valid_subwords)}: They are: {list_of_valid_subwords}" #presents subwords
    return msg

print(best_conjugation("awesomeness"))   #for word in string selects sub words

