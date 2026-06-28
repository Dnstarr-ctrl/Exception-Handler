try:
    age=int(input("Enter your age:- "))
    if age<=0:
     print("INVALID NEGATIVE IS NOT ALLOWED")
except ValueError as age:
    print("INVALID VALUE")
except ZeroDivisionError as age:
    print("Not valid")
except SyntaxError as age:
    print("not allowed")
except IOError as age:
    print("Input/output error")
if age/2==0:
    print("Age is even")
else:
    print("Age is odd")




