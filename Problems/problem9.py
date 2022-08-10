#What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?

#method 1
for i in range(50, 80+1, 10):
	print(i)

#method 2 
print([i for i in range(50, 80+1, 10)])