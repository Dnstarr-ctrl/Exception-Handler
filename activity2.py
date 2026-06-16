try:
    num1,num2=eval(input("Enter 2 numbers. Please note seperate the numbers by comma(,): "))
    opt=(num1/num2)
    print("The result of dividing the 2 numbers is: ", opt)

except SyntaxError as error:
    print("Error! NOT POSSIBLE TO DIVIDE THE NUMBERS GIVEN")
except ZeroDivisionError:
    print("Error! ZERO DIVISION NOT DEFINED")
except:
    print("Error 2319!")
finally:
    print("DO NOT GIVE UP GIVE THE CORRECT INPUT!")