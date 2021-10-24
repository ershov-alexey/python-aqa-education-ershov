mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
#print string
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
#print float
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
#print int