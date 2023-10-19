# Runestone.Academy thinkcspy course
# Chapter 10
# Problem 3

myList = [76, 92.3, 'hello', True, 4, 76]

# Your code here

myList += ["apple"]
myList.insert(3, "cat")
myList.insert(0, 99)
print(myList)

print(myList.index("hello"))
print(myList.count(76))

myList.remove(76)
myList.pop(myList.index(True))

print(myList)