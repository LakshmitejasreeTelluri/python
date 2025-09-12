def second_largest(numbers):
	unique=list(set(numbers))
	if len(unique)<2:
		return none
	unique.sort()
	return unique[-2]
l=[6,19,11,4,5,20,25]
print("second largest number:",second_largest(l))
