# Runestone.Academy thinkcspy course
# Chapter 11
# Problem 2

sdfile = open("studentdata.txt", "r")

for line in sdfile:
    student = line.split()
    sum = 0
    avg = 0
    count = len(student[1:])
    
    for grade in student:
        if grade != student[0]:
            sum += int(grade)
            
    avg = sum/count
    
    print(student[0], "-", avg)
    
sdfile.close()