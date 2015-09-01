# Description: Write a program that prints the sum of the lengths of the names in names.txt.
# Source: http://zarkonnen.com/python_exercises

with open('names.txt', 'r') as f:
	lengths = map(lambda x: len(x) - 1, f) # len(x) - 1: disregard '\n' when computing the name's length 
print sum(lengths)