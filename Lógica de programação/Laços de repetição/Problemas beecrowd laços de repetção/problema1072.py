n= int(input())
ta_in= 0
ta_out = 0
for i in range(n):
    x= int(input())
    if 10<=x<=20:
        ta_in +=1
    else:
        ta_out+=1
print(f"{ta_in} in")
print(f"{ta_out} out")