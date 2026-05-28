n = int(input())
for i in range(n):
    x= int(input())
    if x == 0:
        print("Null")
    elif x % 2==0 and x>0:
        print("Even positive")
    elif x %2==0 and x<0:
        print("Even negative")
    elif x%2!=0 and x>0:
        print("ODD positive")
    elif x%2!=0 and x<0:
        print("ODD negative")