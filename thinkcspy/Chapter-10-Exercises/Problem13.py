# Runestone.Academy thinkcspy course
# Chapter 10
# Problem 13

def count(lst):
    count = 0
    
    for num in lst:
        count += 1
        
    return count

    
def findIn(item, lst):
    pos = 0
    inLst = False
    
    while pos < len(lst) and not inLst:
        if lst[pos] == item:
            inLst = True
        else:
            pos += 1
            
    return inLst
            
     
def reverse(lst):
    newlist = []
    
    for num in lst:
        newlist = [num] + newlist
        
    return newlist
    
    
def index(item, lst):
    pos = 0
    
    for num in lst:
        if num == item:
            return pos
        else:
            pos += 1
            
    return "Item not found."


def insert(pos, item, lst):
    
    newlst = lst[:pos] + [item] + lst[pos:]
    
    return newlst


myList = ["apple", 5, 6, True, "purple", False, "mushroom", 11, "gen-x", "sam", 7, 10, "cause", "interim"]

print(count(myList))
print(findIn("purple", myList))
print(findIn(99, myList))
print(reverse(myList))
print(index(False, myList))
print(index("jello", myList))
print(insert(5, 7.89, myList))