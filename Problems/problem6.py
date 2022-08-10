#Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
def odd_squares_sum(n):
	
	for i in range(1, n):
		if i % 2 == 1:
			odd_squares.append(i**2)

odd_squares = []
n = int(input())
odd_squares_sum(n)
print(sum(odd_squares))