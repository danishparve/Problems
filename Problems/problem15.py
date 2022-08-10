#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).
def is_distinct(list):
	return len(list) == len(set(list))
	
list = [1, 2, 3, 3, 5]
print(is_distinct(list))