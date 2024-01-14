#open a file
f=open("gayu.txt")#it cant open sobread it
#read
print(f.read())
#or
one=f.read()
print(one)
#write inside the file
#f.write()-error so first we have to open the file and use the module w
f=open("gayu.txt","w")
f.write("nila\n")
f.write("ji\n")
f.close()#file must close after every action
#when you enter the valu second file it cant br read so we use r+ mean read and write
f=open("gayu.txt","r+")
print(f)
#to store already typed value in the file ,we use append a
f=open("gayu.txt","a")
f.write("hiii")
f.close()
f=open("gayu.txt","r+")
