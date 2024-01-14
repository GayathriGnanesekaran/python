user={
    "name" : "gayu",

     "gender" : "female"
    }
print(user)
print(type(user))
#access  the element  using key
print(user["name"])
print(user["gender"])
#to get keys
print(user.keys())
#to get values
print(user.values())
#to get key and value
print(user.items())
#for loop
for x in user.keys():
    print(x)
for x in user.values():
    print(x)
for x,y in user.items():
    print(x,y)
#to checck particular value
if "age" in user:
    print("present")
else:
    print("not present")
#add value using update fun
user.update({"age":23})
print(user)
#change the value using index
user["age"]=45
print(user)
user.clear()
del (user)
#multiple dictionary
users={
    "user1":
        { 
        "name":"agyu",
        "age":233
        },
    "user2":
        {
        "name":"yyy",
        "age":43
        }
    }
print(users)

    

