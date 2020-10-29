#ISBN
## variable input and numerical check
isbn=input("input 12 digit isbn number ")
isbn=isbn.replace('-','') #replaces spaces with -
#isbn=list(map(int,isbn)) #converts input to list of defined integer elements
digit_12 = 10 - ((isbn[0] +(3*isbn[1]) + isbn[2] + (3*isbn[3]) + isbn[4] +(3*isbn[5]) +isbn[6] + (3*isbn[7]) + isbn[8] +(3*isbn[9]) +isbn[10] +(3*isbn[11]))%10) #checks digit
isbn.append(digit_12) #adds 12th digit to end of isbn

## isbn output
print("ISBN:")
a=isbn[0],isbn[1],isbn[2], '-' ,isbn[3],isbn[4],isbn[5],'-',isbn[6],isbn[7],isbn[8],'-',isbn[9],isbn[10],isbn[11],'-',isbn[12] #defines elements in correct format
b=''.join(map(str,a)) #defines elements as a string
print(b) #printing full isbn number
