# Description: Write a program that reads in the names in names.txt and writes out a file at names_sorted.txt containing them sorted alphabetically.
# Source: http://zarkonnen.com/python_exercises

with open('names.txt', 'r') as f1:
	with open('names_sorted.txt', 'w') as f2:
		for i in sorted(f1):
			f2.writelines(i)