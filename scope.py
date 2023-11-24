a = 250

def f1 ():
    global a
    a = 100 # This is a global variable
    print(a)

def f2():
    a = 50 # This is a local variable
    print(a)

f1()
f2()
print(a)
