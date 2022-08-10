#Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
def minmax(data):
	a = data[0]
	for i in data:
		if a >= i:
			a = i
	list.append(a)
	
	b = data[0]
	for j in data:
		if b <= j:
			b = j
	list.append(b)

list = []
data = input().split()
minmax(data)
print(tuple(list))