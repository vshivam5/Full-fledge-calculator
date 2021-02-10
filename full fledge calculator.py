import array as arr
import math
try:
    num = int(input("Enter the total numbers of element: "))
except Exception as e:
    print(e)
    exit()
a = arr.array('i',[])
for i in range(num):
    try:
        element = int(input("Element: "))
    except Exception as e:
        print(e)
        exit()
    a.append(element)
choice = input("""\nEnter operation\n
1)For Addition press +\n2)For Division press /\n3)For Multiplication press *\n4)For Substraction press - \n\n""")
for i in range(num):
    if choice == "+":
        print("\nYou Entered `+` for Addition\n")
        print("The Addition of elements is: ",sum(a))
        exit()
        break
    elif choice == "/":
        print("\nYou Entered `/` for Division\n")
        for i in a:
            data = a[num-num]/a[(num+1)-num]
        if num == 2:
            print("The Division of elements is: ",data)
            print("Round of result is : ",round(data))
            exit()
            break
        else:
            new = data/a[(num+2)-num]
            if num == 3:
                print("The Division of elements is: ",new)
                print("Round of result is : ",round(new))
                exit()
                break
            elif num == 4:
                num = num-1
                new = new/a[(num+3)-num]
                print("The Division of elements is: ",new)
                print("Round of result is : ",round(new))
                exit()
                break
            elif num == 5:
                data = a[num-num]/a[(num+1)-num]
                data = data/a[(num+2)-num]
                data = data/a[(num+3)-num]
                data = data/a[(num+4)-num]
                print("The Division of elements is: ",data)
                print("Round of result is : ",round(new))
                exit()
                break
            elif num == 6:
                data = a[num-num]/a[(num+1)-num]
                data = data/a[(num+2)-num]
                data = data/a[(num+3)-num]
                data = data/a[(num+4)-num]
                data = data/a[(num+5)-num]
                print("The Division of elements is: ",data)
                exit()
                exit()
                break
            elif num == 7:
                data = a[num-num]/a[(num+1)-num]
                data = data/a[(num+2)-num]
                data = data/a[(num+3)-num]
                data = data/a[(num+4)-num]
                data = data/a[(num+5)-num]
                data = data/a[(num+6)-num]
                print("The Division of elements is: ",data)
                print("Round of result is : ",round(new))
                exit()
                break
            elif num == 8:
                data = a[num-num]/a[(num+1)-num]
                data = data/a[(num+2)-num]
                data = data/a[(num+3)-num]
                data = data/a[(num+4)-num]
                data = data/a[(num+5)-num]
                data = data/a[(num+6)-num]
                data = data/a[(num+7)-num]
                print("The Division of elements is: ",data)
                print("Round of result is : ",round(new))
                exit()
                break
            elif num == 9:
                data = a[num-num]/a[(num+1)-num]
                data = data/a[(num+2)-num]
                data = data/a[(num+3)-num]
                data = data/a[(num+4)-num]
                data = data/a[(num+5)-num]
                data = data/a[(num+6)-num]
                data = data/a[(num+7)-num]
                data = data/a[(num+8)-num]
                print("The Division of elements is: ",data)
                print("Round of result is : ",round(new))
                exit()
                break
            else:
                data = a[num-num]/a[(num+1)-num]
                data = data/a[(num+2)-num]
                data = data/a[(num+3)-num]
                data = data/a[(num+4)-num]
                data = data/a[(num+5)-num]
                data = data/a[(num+6)-num]
                data = data/a[(num+7)-num]
                data = data/a[(num+8)-num]
                data = data/a[(num+9)-num]
                print("The Division of elements is: ",data)
                print("Round of result is : ",round(new))
                exit()
                break
    elif choice == "*":
        print("\nYou Entered `*` for Multiplication\n")
        for i in a:
            data = a[num-num]*a[(num+1)-num]
        if num == 2:
            print(data)
            exit()
            break
        else:
            new = data*a[(num+2)-num]
            if num == 3:
                print("The Multiplication of elements is: ",new)
                exit()
                break
            elif num == 4:
                num = num-1
                new = new*a[(num+3)-num]
                print("The Multiplication of elements is: ",new)
                exit()
                break
            elif num == 5:
                data = a[num-num]*a[(num+1)-num]
                data = data*a[(num+2)-num]
                data = data*a[(num+3)-num]
                data = data*a[(num+4)-num]
                print("The Multiplication of elements is: ",data)
                exit()
                break
            elif num == 6:
                data = a[num-num]*a[(num+1)-num]
                data = data*a[(num+2)-num]
                data = data*a[(num+3)-num]
                data = data*a[(num+4)-num]
                data = data*a[(num+5)-num]
                print("The Multiplication of elements is: ",data)
                exit()
                break
            elif num == 7:
                data = a[num-num]*a[(num+1)-num]
                data = data*a[(num+2)-num]
                data = data*a[(num+3)-num]
                data = data*a[(num+4)-num]
                data = data*a[(num+5)-num]
                data = data*a[(num+6)-num]
                print("The Multiplication of elements is: ",data)
                exit()
                break
            elif num == 8:
                data = a[num-num]*a[(num+1)-num]
                data = data*a[(num+2)-num]
                data = data*a[(num+3)-num]
                data = data*a[(num+4)-num]
                data = data*a[(num+5)-num]
                data = data*a[(num+6)-num]
                data = data*a[(num+7)-num]
                print("The Multiplication of elements is: ",data)
                exit()
                break
            elif num == 9:
                data = a[num-num]*a[(num+1)-num]
                data = data*a[(num+2)-num]
                data = data*a[(num+3)-num]
                data = data*a[(num+4)-num]
                data = data*a[(num+5)-num]
                data = data*a[(num+6)-num]
                data = data*a[(num+7)-num]
                data = data*a[(num+8)-num]
                print("The Multiplication of elements is: ",data)
                exit()
                break
            else:
                data = a[num-num]*a[(num+1)-num]
                data = data*a[(num+2)-num]
                data = data*a[(num+3)-num]
                data = data*a[(num+4)-num]
                data = data*a[(num+5)-num]
                data = data*a[(num+6)-num]
                data = data*a[(num+7)-num]
                data = data*a[(num+8)-num]
                data = data*a[(num+9)-num]
                print("The Multiplication of elements is: ",data)
                exit()
                break
    elif choice == "-":
        print("\nYou Entered `-` for Substraction\n")
        for i in a:
            data = a[num-num]-a[(num+1)-num]
        if num == 2:
            print(data)
            exit()
            break
        else:
            new = data-a[(num+2)-num]
            if num == 3:
                print("The subtraction of elements is: ",new)
                exit()
                break
            elif num == 4:
                num = num-1
                new = new-a[(num+3)-num]
                print("The subtraction of elements is: ",new)
                exit()
                break
            elif num == 5:
                data = a[num-num]-a[(num+1)-num]
                data = data-a[(num+2)-num]
                data = data-a[(num+3)-num]
                data = data-a[(num+4)-num]
                print("The subtraction of elements is: ",data)
                exit()
                break
            elif num == 6:
                data = a[num-num]-a[(num+1)-num]
                data = data-a[(num+2)-num]
                data = data-a[(num+3)-num]
                data = data-a[(num+4)-num]
                data = data-a[(num+5)-num]
                print("The subtraction of elements is: ",data)
                exit()
                break
            elif num == 7:
                data = a[num-num]-a[(num+1)-num]
                data = data-a[(num+2)-num]
                data = data-a[(num+3)-num]
                data = data-a[(num+4)-num]
                data = data-a[(num+5)-num]
                data = data-a[(num+6)-num]
                print("The subtraction of elements is: ",data)
                exit()
                break
            elif num == 8:
                data = a[num-num]-a[(num+1)-num]
                data = data-a[(num+2)-num]
                data = data-a[(num+3)-num]
                data = data-a[(num+4)-num]
                data = data-a[(num+5)-num]
                data = data-a[(num+6)-num]
                data = data-a[(num+7)-num]
                print("The subtraction of elements is: ",data)
                exit()
                break
            elif num == 9:
                data = a[num-num]-a[(num+1)-num]
                data = data-a[(num+2)-num]
                data = data-a[(num+3)-num]
                data = data-a[(num+4)-num]
                data = data-a[(num+5)-num]
                data = data-a[(num+6)-num]
                data = data-a[(num+7)-num]
                data = data-a[(num+8)-num]
                print("The subtraction of elements is: ",data)
                exit()
                break
            else:
                data = a[num-num]-a[(num+1)-num]
                data = data-a[(num+2)-num]
                data = data-a[(num+3)-num]
                data = data-a[(num+4)-num]
                data = data-a[(num+5)-num]
                data = data-a[(num+6)-num]
                data = data-a[(num+7)-num]
                data = data-a[(num+8)-num]
                data = data-a[(num+9)-num]
                print("The subtraction of elements is: ",data)
                exit()
                break
else:
    print("Invalid choice")
    print("Choose from the Given operations")
    print("Press OK !")
    quit()
