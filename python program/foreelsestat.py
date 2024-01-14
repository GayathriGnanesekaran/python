for i in range(5):
    print(i)
else:
    print("loop completed")
#not satisfies
for j in range(5):
    if j==4:
        break
    print(j)
    j+=1
else:
    print("loop completed")
