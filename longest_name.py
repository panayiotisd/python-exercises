# Description: The file names.txt contains a list of names, one per line. Write a program that reads in this list and prints the longest name.
# Source: http://zarkonnen.com/python_exercises

with open('names.txt', 'r') as f:
	longest_name = ""
	while True:
		name = f.readline()
		if name == "":
			break
		if len(name) > len(longest_name):
			longest_name = name
print longest_name