#nested decisions in python
#multi-decisions program!

print("*** welcome to netflix***")

name=input("Enter your name:")
email=input("enter your email:")
password=input("enter your password:")
age=int(input("enter your age:"))

if age >=18:
    print(f"dear{name},welcome to Netflix!")
    if email=="sheri234@gmail.com" and password=="sheri123":
       print(f"dear:{name},welcome to the netflix sessions, please select category")
     
    elif email=="noor234@gmail.com" and password=="mahnoor123":
       print(f"dear:{name},welcome to the netflix sessions, please select category")
    
    elif email=="gopu34@gmail.com" and password=="nasir23":
       print(f"dear:{name},welcome to the netflix sessions, please select category")
       
    elif email=="farwa@gmail.com" and password=="farwa000":
       print(f"dear:{name},welcome to the netflix sessions, please select category")
       
    elif email=="humaaj@gmail.com" and password=="huma03":
       print(f"dear:{name},welcome to the netflix sessions, please select category")
       
    elif email=="umar@gmail.com" and password=="umar993":
       print(f"dear:{name},welcome to the netflix sessions, please select category")  
       
    else:
        print(f"Dear {name},welcome to the login credentials are invalid!")
    
else:
    print(f"dear{name},please watch pogo!")