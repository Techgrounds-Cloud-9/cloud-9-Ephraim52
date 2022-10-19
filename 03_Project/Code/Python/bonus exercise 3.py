'''
The output should be:
30
'''

# by changing the foo -= 1 where it kept deducting 1 till it was in range of 10, I made it foo -= -1 so that it kept adding 1 for 10 times. So 20 + 1 x 10 = 30.
foo = 20
for i in range(10):
	foo -= -1

print(foo)