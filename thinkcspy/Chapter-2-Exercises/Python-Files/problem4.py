#5Runestone.Academy thinkcspy course
# Chapter 2
# Problem 4

currentDay = input('''Enter the current day using one of the following numbers:
Sunday    = 0
Monday    = 1
Tuesday   = 2
Wednesday = 3
Thursday  = 4
Friday    = 5
Saturday  = 6''')
currentDay = int(currentDay)

stayLength = input('How long is your stay?')
stayLength = int(stayLength)

# Improved upon the long windedness of my answer this time by following the example of the solution 
# in the previous problem
stay = currentDay + stayLength
returnDay = stay % 7

print('It is currently Day', currentDay,'.')
print('Your stay is ', stayLength, 'days long.')
print('You will return on Day', returnDay, '.')
print('''Sunday    = 0
Monday    = 1
Tuesday   = 2
Wednesday = 3
Thursday  = 4
Friday    = 5
Saturday  = 6''')