# Description: Write a program that reads in the names in names.txt and prints all the names that have the length given by the first command-line argument.
# Source: http://zarkonnen.com/python_exercises

import sys
length = int(sys.argv[1])
with open('names.txt', 'r') as f:
	names = filter(lambda x: len(x) == length + 1, f)
	for n in names:
		print n.replace("\n", "")