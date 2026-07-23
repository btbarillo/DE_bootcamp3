#Method	Description
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)


carB = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
carA=carB.copy()
print(carA)


x = ('key1', 'key2', 'key3')
y={1,2,3}

thisdict=dict.fromkeys(x,y)
print(thisdict)


carC = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

carC.get("brand")
print(carC.get("brand"))


carD = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(carD.items())



carE = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
j = carE.keys()
print(j)


carF = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

carF.pop("year")
print(carF)


carG = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

carG.popitem()
print(carG)


carH = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

carH.setdefault("color","Red")
print(carH)


carI = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

carI.update({"color": "White"})
carI["year"]=1997 #alternative way
print(carI)


carJ = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(carJ.values())