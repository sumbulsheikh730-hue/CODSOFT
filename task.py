print("welcome to Simple Calculator!")

a=float(input("enter the value of a :"))
b=float(input("enter the value of b :"))

x=str(input("enter the arithematic operation (+,-,/,*):"))
Result= None
match x:
    case"+":
        Result=a+b
        print(f"{a} + {b} = {Result}")
    case "-":
        Result=a-b
        print(f"{a} - {b} = {Result}")
    case "/":
        Result=a/b
        print(f"{a} / {b} = {Result}")
    case "*":
        Result=a*b
        print(f"{a} * {b} = {Result}")
    case _ :
        print(" your value is invalid")
if Result is not None:
    print(f" the result is :{Result}")