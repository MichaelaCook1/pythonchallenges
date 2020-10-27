## defining function "near" to find string 2 within string 1 where an element has been removed 
def near(string1,string2):
    list1 = list(string1) #converts first input into a list
    list2 = list(string2) #converts second input into a list
    for index in range(len(list1)):     #sets letter index for all letters in first input
        element_to_remove = list1[index] #defines letter removed from the first input
        del list1[index] #deletes said letter
        if list1 == list2: #are the inputs equivalent when one letter is removed from first input
            return True 
        list1.insert(index, element_to_remove) #inputs are not equivalent after letter removal
    return False

word1 = input("enter first word: ") 
word2 = input("enter second word: ")

print(near(word1,word2)) #prints both inputs and result of near function