def enterage(age):
    
    if age<0:
        raise ValueError("Only positive integers are aollowed")
    
    if age%2==0:
        print("Age is even")
        
    else:
        print("Age is odd")
        
try:
    num=int(input("Enter your age: "))
    enterage(num)
    
except ValueError:
    print("Only Positive integers are allowed")