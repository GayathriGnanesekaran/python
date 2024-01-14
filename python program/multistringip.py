gayu=["23","45","67"]
print(gayu)
print(gayu[0])
print("||".join(gayu))# we use several instaed of|| to display as we wish
#to get multiline inputs
para=[]
print("enter the para")
while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
    print(para)
    output='\n'.join(para)#we use another symbols also
    print(output)
    

        
