'''
The output should be:
there are 0 kids on the street
there are 1 kids on the street
there are 2 kids on the street
there are 3 kids on the street
there are 4 kids on the street
'''

# the counting for range or the amount of times something needs to do the while loop like here always starts at 0. It never starts at 1 unless specified.
# So I changed while foo <= 5: to what it is now and it counts up to the correct amount of times.
foo = 0
while foo <= 4:
	print('there are', foo, 'kids on the street')
	foo += 1