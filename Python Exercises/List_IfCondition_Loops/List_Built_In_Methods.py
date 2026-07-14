#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list


fruits = ['apple', 'banana', 'cherry']
fruits.append("grapes")
print(fruits)

a = ["apple", "banana", "cherry"]
a.clear()
print(a)

b = ["apple", "banana", "cherry"]
g=b.copy()
print(g)


c = ["apple", "banana", "cherry","banana"]
c.count("apple")
print(c.count("banana"))


d = ["apple", "banana", "cherry"]
f = ["kiwi", "tomato"]
d.extend(f)
print(d)


e = ["apple", "banana", "cherry"]
e.insert(1,"mango")
print(e)


h = ["apple", "banana", "cherry"]
h.pop(1)
print(h)


j = ["apple", "banana", "cherry"]
j.remove("cherry")
print(j)

k = ["apple", "banana", "cherry"]
k.reverse()
print(k)


l = ["apple", "mango", "zuchini", "banana", "cherry"]
l.sort()
print(l)


def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW'] #sorted the list based on the length of the elements

cars.sort(key=myFunc)
print(cars)