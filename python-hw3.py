def predicate(x):
	if x > 50 and x % 2 != 0:
		return True
	else:
		return False

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

print(filter(predicate, numbers))