'''
The output should be:
hello Casper
hello Floris
hello Esther
'''

#replaced the 'l' from loo to 'f' to make the variable foo. So that it prints the value hello infront of the variable name which has the values that contains 3 different names.
foo = 'hello'
ls = ['Casper', 'Floris', 'Esther']
for name in ls:
	print(foo ,name)