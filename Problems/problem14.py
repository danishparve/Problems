#Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.
def prod_odd(list):
	
	for i in list:
		for j in list:
			if i*j % 2 == 1:
				pairs.append([i, j])
	return pairs

list = [a for a in range(0, 10)]
pairs = []
print(prod_odd(list))