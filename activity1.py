try:
    num=int(input("Enter any number: "))
    print("The number you entered has no errors:",num)
except ValueError as num:
    print("Error! VALUE ENTERED IS NOT OF INTEGER TYPE: ",num)
