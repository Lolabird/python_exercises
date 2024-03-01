# Runestone.Academy thinkcspy course
# Chapter 16
# Problem 2

def reverseList(lst):
    if len(lst) == 1:
        return lst
    else:
        lst = [lst[-1]] + reverseList(lst[:-1])
        return lst