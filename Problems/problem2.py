#Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
def is_even(k):
	
	return (not(k & 1))

k = int(input())
print('Even') if is_even(k) else print('Odd')