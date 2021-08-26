import sys

ladder = int(input())

for i in range(ladder + 1):
	print(((ladder - i) * " ") + (i * "#"))
	i += 1	