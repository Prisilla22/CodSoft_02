def addition():
    a=n1+n2
    print("Your Answer=",a)
def subtraction():
    s=n1-n2
    print("Your Answer=",s)
def multi():
    m=n1*n2
    print("Your Answer=",m)
def div():
    d=n1/n2
    print("Your Answer=",d)
def modules():
    mo=n1%n2
    print("Your Answer=",mo)
def operation():
    print("-------The Operations You want-------")
    print("1. Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modules")
    op=int(input("Enter the operation "))

    while True:
        if(op==1):
             addition()
        elif(op==2):
            subtraction()
        elif(op==3):
            multi()
        elif(op==4):
            div()
        elif(op==5):
            modules()
        else:
            (print("Invalid Input"))
     
        next_op=input("Want to do next operation?(yes/no): ")
        if next_op=="no":
            exit()
        elif next_op=="yes":
            operation()
        else:
            print("Invalid Input")

n1=float(input("Enter the first number you want "))
n2=float(input("Enter the second number you want "))
operation()