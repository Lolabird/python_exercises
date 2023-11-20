# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 7

P = 10000 
n = 12
r = 0.08
n = 12

# Noticed that they gave separate variables to the inputs problem 3 and
# the converted ints so decided to do the same here.
t_string = input('For how many years will your principal be earning interest?')
t = int(t_string)

A = P*(1+r/n)**(n*t)

print('The final amount after you will earn after', t, 'years is', A)