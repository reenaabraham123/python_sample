a = "How are you?"

print(bool(0))

x = ("apple", "banana", "cherry")
print(type(x))

print("1-biriyani","2-meals","3-pizza","4-burger","5-juice")
order = input("please order a menu")
if order == '1':
    print("biriyani ready");
elif order == '2':
    print("meals ready")
elif order == '3':
    print("pizza ready")
elif order == '4':
    print("burger ready")
elif order == '5':
    print("juice ready")
else:
    print("not available")

n = 4
for i in range (n):
         print("  "*(n-i)+"*"*((2*i)+1))







