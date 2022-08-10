#Write a short Python function that counts the number of vowels in a given character string.
def vowels(string):
	vowel = ['a', 'e', 'i', 'o', 'u']
	count = 0
	for i in string:
	    for j in vowel:
	    	if i == j:
	    		count += 1
	return count 
string = input('Enter a string: ').lower()
print('Number of vowels in the string is: ' +str(vowels(string)))