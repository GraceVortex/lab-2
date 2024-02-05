"""
+, /, *, //, %

** - degree

"""
x = 7
print(x < 5 and  x < 10)
x = 7
print(x < 5 or  x < 10)

x = 5
print(x is 7)

mylist = ["koyan", "ayu"]
print("koyan" in mylist)
print("maugly" not in mylist)

#Bitwise operators
x = 6
y = 3
print(x & y) #answ is 2 'cause 110*011 = 010 = 2
print(x|y) #answ is 7 'cause 110+011 = 111 = 7
print(x^y) #ans is 5 ->assigns 1 iff one of the el's is 1
print(~x) #inverts
print(x<<2)
print(x>>2)