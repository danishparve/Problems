#Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
def sum_squares(n):
	
	for i in range(1, n):
		squares.append(i**2)

squares = []
n = int(input())
sum_squares(n)
print(sum(squares))