#library book renewal fine amout
'''
0=no fine
1-5 days=0.5
5-10 days=1
10-30 days=5
>30=membership cancel
'''
days=int(input("enter the number of days:"))
if days==0:
  print("no fine")
elif(days>=1 and days<=5):
  print("fine amount is",days*0.5)
elif(days>5 and days<=10):
  print("fine amount is",days*1)
elif(days>10 and days<=30):
  print("fine amount is",days*5)
else:
  print("membership cancel")
