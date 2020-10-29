##times-tables


n=10 #number of tables
for row in range(1,n+1): #defines rows
    for col in range(1,n+1): #defines columns
        print(row*col, end="\t") #performs operation "end" for formatting
    print()
