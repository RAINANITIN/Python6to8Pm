x = int(input("Enter Ist number:"))
y = int(input("Enter 2nd number:"))
Negative = input("Enter parameter")

if Negative=="true":
    if x<0 and y<0:
        print("True")
    else:
        print("False")
else:
    if x<0 or y>0 or y<0 or x>0:
        print("True")
    else:
        print("False")
