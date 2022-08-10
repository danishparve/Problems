#Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.
def reverse(data):
	
	n = len(data) - 1
	for i in range(n, -1, -1):
		reversed.append(data[i])
	return reversed

reversed = []
data = [j for j in range(0, 30, 3)]
print(data)
print(reverse(data))