thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

x = thisdict.get("model")
x = thisdict.keys()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

x = thisdict.values()
x = thisdict.items()

thisdict["year"] = 2018
thisdict.update({"year": 2020})

thisdict.update({"color": "red"})
thisdict.pop("model")
thisdict.popitem()
del thisdict["model"]
for x in thisdict:
  print(x)
for x in thisdict.values():
  print(x)
for x, y in thisdict.items():
  print(x,y)

  
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict) #copy


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])

'''Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary'''
