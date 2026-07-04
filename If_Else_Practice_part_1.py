num =int(input("input a number: "))
if num / 2 ==0:
    print (num ,"is a odd number")
else:
    print (num,"is a even number")

#=========== Odd even check============


num = int(input( "enter a number: " ))

if (num>0):
    print(num, " is a positive number")
else:
    print(num, " is a negative number")

#======== positive Negative check =========


a = int(input("enter a number "))
b = int(input("enter a number "))
if (a>b):
    print("Large number is :" ,a)
else:
    print("Large number is :" ,b)

#======== find the large number ========


studentNum = int(input("Enter the number: "))
if studentNum <= 40:
    print("Fall")
else:
    print("Pass")

#============ Pass or fail ===========


studentNum = int(input("Enter the Age: "))
if studentNum >= 18:
   print("you can vote")
else:
    print("Sorry you can't vote")

#============ Vote or Not ===========

a =int(input("enter a number"))
b =int(input("enter a number"))
c =int(input("enter a number"))
if a<b and a<c:
    print(a, "is the largest")
elif b>a and b>c:
    print(b, "is the largest")
elif c>a and c>b:
    print(c, "is the largest")

#============ Largest Number  ===========


studentNum = int(input("Enter the number: "))
if studentNum <40:
    print("Fail")
elif studentNum > 40 and studentNum < 49:
    print("Result is C")
elif studentNum > 50 and studentNum <59:
    print("Result is B")
elif studentNum > 60 and studentNum <69:
    print("Result is A-")
elif studentNum > 70 and studentNum <79:
    print("Result is A")
elif studentNum > 80 and studentNum <100:
    print("Result is A+")
elif studentNum > 100:
    print("Wrong Input")

#=============== Student Grate =============


user_name= "siam222"
passWord ="siamm222"
Username = input("Enter the Username: ")
Password = input("Enter the Password: ")

if Username == user_name and Password == passWord:
    print("Login Successful")
else:
    print("Try Again")

#=============== Login Condition =============


num =int(input("input a number: "))
if num % 3== 0 and num % 5== 0:
    print("The number is divisible by 3 and 5.")
else:
    print("not divisible by 3 and 5.")

#=============== Number divisible =============


Year = int(input( "input the Year :-"))
if Year % 400 == 0:
    print("This is Leap Year")
elif Year % 100 == 0:
    print("This is not a Leap Year")
elif Year % 4== 0:
    print("This is Leap Year")
else:
    print("This is not a Leap Year")

