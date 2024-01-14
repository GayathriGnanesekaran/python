#try catch
try:
  a=100/0
  print(a)
except Exception as e:
    print(e)
#try catch else block
try:
    a=10/10
    print(a)
except Exception as e:
    print(e)
else:
    print(a)
#finally
try:
    a=10/0
    print(a)
except Exception as w:
    print(w)
else:
    print(a)
finally:
    print("good")
#to print total number of error in pythhon
print(dir(locals()["__builtins__"]))

