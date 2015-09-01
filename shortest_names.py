# Description: Write a program that prints the shortest names in names.txt, one on each line. There is more than one shortest name, so both need to be printed.
# Source: http://zarkonnen.com/python_exercises

with open('names.txt', 'r') as f:
	lengths = map(lambda x: len(x) - 1, f) # len(x) - 1: disregard '\n' when computing the name's length
	shortest = sorted(lengths)[0]
	f.seek(0)	# reset the file pointer
	names = filter(lambda x: len(x) == shortest + 1, f)
for n in names:
	print n.replace("\n", "")