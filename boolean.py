print(9>99)
print(9==99)
print(9<99)



a = 99
b = 31
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")



print(bool("kohlarn"))
print(bool())
print(bool(14))
print(bool(0))
print(bool["apple", "banan", "lolo"])
print(bool(["apple", "banan", "lolo"]))

#examples of false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#examples of false

class myclass():
  def __len__(self):
    return 0



myobj = myclass()
print(bool(myobj))




def func():
   return True
print(func())



def func():
   return True
if not func():
   print("No")
else:
   print("Yes")


x = 5.3
print(isinstance(x, int))







