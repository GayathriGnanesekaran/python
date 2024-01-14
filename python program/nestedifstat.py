'''
3 marks as inputt
total
average
result
if pass grade
 90-100 a
 80-89 b
 70-79 c
 else d
 '''
n1=int(input("enter first marks:"))
n2=int(input("enter ssecond marks:"))
n3=int(input("enter three marks:"))
total=n1+n2+n3
print(total)
average=total/3
print(average)
if n1>=35 and n2>=35 and n3>=35:
    print(" result is pass")
    if(average>=90 and average<=100):
        print("grade a")
    elif(average>=80 and average<=89):
        print("grade b")
    elif(average>=70 and average<=79):
        print("grade c")
    else:
        print("grade d")
else:
    print("result is fail")
    print("no grade")
        
