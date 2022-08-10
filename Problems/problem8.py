#Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index −n≤k< 0, what is the equivalent index j ≥0 such that s[j] references the same element?
n = 'Thisisastring'
k = int(input('Enter a negative index: '))
print('n[k]: ' + n[k])
j = k + len(n)
print('n[j]: ' + n[j])