# Description: Write a program that reads in the names in names.txt and writes out a file at names_sorted_by_length.txt containing them sorted by length.
# Source: http://zarkonnen.com/python_exercises

with open('names.txt', 'r') as f1:
	with open('names_sorted_by_length.txt', 'w') as f2:
		for i in sorted(f1, cmp=lambda x, y: 1 if len(x) > len(y) else 0 if len(x) == len(y) else -1):
			f2.writelines(i)