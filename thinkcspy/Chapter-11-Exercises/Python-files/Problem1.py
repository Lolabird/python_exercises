# Runestone.Academy thinkcspy course
# Chapter 11
# Problem 1

sdfile = open("studentdata.txt", "r")

for line in sdfile:
    student = line.split()
    if len(student[1:]) > 6:
        print(student[0])
    
sdfile.close()