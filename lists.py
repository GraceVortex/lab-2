mylist = ["donda", "mbdtf", "yandhi"]
print(mylist)

#since list is indexed then we may duplicate
mylistdupl = ["donda", "donda", "donda"]

len(mylist) #to know how many items

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

print(type(mylist)) #<class 'list'>

thislist = list(("apple", "banana", "cherry")) 
print(thislist)

print(mylist[1])
print(mylist[-1])
print(mylist[2:5]) #w/o 5

mylist = ["donda", "mbdtf", "yandhi"]
mylist[1] = "graduation"
print(mylist)

#we may change the range if list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]
thislist.insert(1, "passionfruit")
thislist.append("vultures")

listtoadd = ["cruelsummer"]

thislist.extend(listtoadd)  
thislist.remove("vultures")
thislist.pop(1) #==thislist.del(1)
thislist.pop()
del thislist

thislist.clear() #list is empty but still remains

print(thislist)

epstlist = ["djt", "mj", "bc"]
for i in epstlist:
    print(i)

for i in range(1,2):
    print(epstlist[i])

i = 0
while i < len(epstlist):
    print(epstlist[i])
    i+=1

[print(x) for x in thislist]

yealbums = ["donda", "grad", "mbdtf"]
alm = []
for i in yealbums:
    if "a" in i:
        alm.append(i)
print(alm)

alm = [i for i in yealbums if "a" in i]

#newlist = [expression for item in iterable if condition == True]
newlist = [x if x != "banana" else "orange" for x in fruits]



highlist = ["orange", "apple", "passionfruit"]
highlist.sort()
highlist.sort(reverse = True)
print(highlist)

def mifunc(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = mifunc)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


mycopy = thislist.copy()
mycopy = list(thislist)



