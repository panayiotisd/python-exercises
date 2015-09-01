# Description: Write a program that reads in the names in names.txt and writes out a file at name_lengths.txt containing the length of each name, one per line, in the corresponding order.
# Source: http://zarkonnen.com/python_exercises

with open('names.txt', 'r') as f:
	lengths = map(lambda x: len(x) - 1, f) # len(x) - 1: disregard '\n' when computing the name's length 
with open('name_lengths.txt', 'w') as f:
	for l in lengths:
		f.write(str(l) + '\n')