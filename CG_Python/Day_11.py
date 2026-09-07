#Day - 11

'''
-> elif: it is used to check multiple conditions.
    -> Syntax = if condition:
                    Statement_1 
                elif condition:
                    Statement_2
                else:
                    Statement_3
    -> example: a = 10 
                b = 20
                c = 30
                if a == b:
                    print("a is equal to b")
                elif a == c:
                    print("a is equal to c")
                else:
                    print("a is not equal to b or c")

-> nested if: it is used to check conditions inside a if statement.
    -> Syntax = if condition:
                    if condition:
                        statement_1
                    else:
                        statement_2
                else:
                    statement_3
    -> example: if 10 > 5:
                    if 20 > 10:
                        print("20 is greater than 10")
                    else:
                        print("20 is less than 10")
                else:
                    print("10 is less than 5")

-> Example Programs:

    -> Even or Odd:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

    -> Grading System:
        Marks = int(input("Enter Marks: "))
        if Marks >= 90:
            print("Grade A+")
        elif Marks >= 80:
            print("Grade A")
        elif Marks >= 70:
            print("Grade B+")
        elif Marks >= 60:
            print("Grade B")
        elif Marks >= 50:
            print("Grade C+")
        elif Marks >= 40:
            print("Grade C")
        elif Marks >= 35:
            print("Grade D")
        else:
            print("Fail")

    -> 


'''
