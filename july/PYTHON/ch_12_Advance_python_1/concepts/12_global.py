a=98

def func():
    global a  # This will refer to the global variable 'a'
    a=32
    print(a)

func()
print(a)  # This will print 98, the global variable 'a'
# The function 'func' has its own local variable 'a', which does not affect the