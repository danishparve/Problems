#Give a single command that computes the sum from Problem6, relying on Python’s comprehension syntax and the built-in sum function.
n = int(input())
print(sum(i**2 for i in range(1, n) if i % 2 == 1))