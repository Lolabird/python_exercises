# Runestone.Academy thinkcspy course
# Chapter 11
# Problem 3

sdfile = open("studentdata.txt", "r")

for line in sdfile:
    student = line.split()
    mingrade = student[1]
    maxgrade = student[1]
    
    for grade in student:
        if grade != student[0]:
            if int(grade) < int(mingrade):
                mingrade = grade
            if int(grade) > int(maxgrade):
                maxgrade = grade
                
    outputText = "{} - minimum score:{}; maximum score:{}".format(student[0], mingrade, maxgrade)
                
    print(outputText)
    
sdfile.close()