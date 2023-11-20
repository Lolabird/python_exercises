# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 3


currentTime = input('What time is it?')
currentTime = int(currentTime)

waitTime = input('In how many hours do you need to wake up?')
waitTime = int(waitTime)

print('It is currently', currentTime,'.')
print('You need to wake up in', waitTime, 'hours.')

# My solution was more long winded than the actual answer, but it still works!
totalTime = currentTime + waitTime
time24hr = totalTime // 24
alarmTime = totalTime - 24 * time24hr

print('The alarm has been set for', alarmTime, '.')