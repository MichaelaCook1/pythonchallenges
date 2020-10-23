#Grade Calculator
pgrade = int(input("Enter your physics grade: "))
cgrade = int(input("Enter your chemistry grade: "))
mgrade = int(input("Enter your maths grade: "))
grade = (pgrade + cgrade + mgrade) / 3 

if grade >= 70:
    print("You scored a grade of: A")
elif grade >= 60:
    print("You scored a grade of: B")
elif grade >= 50:
    print("You scored a grade of: C")
elif grade >= 40:
    print("You scored a grade of: D")
else:
    print("You Failed")