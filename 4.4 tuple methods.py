#methods of tuple
# Tuple is immutable, so it has fewer methods than lists
# Concatenation
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print("Concatenated Tuple:", c)
# Repetition
d = a * 3
print("Repeated Tuple:", d)
# Membership Test
print("Is 2 in a?", 2 in a)
# Indexing
print("First element of a:", a[0])
# Slicing
print("Slice of a from index 1 to 2:", a[1:3])
# Length
print("Length of a:", len(a))
# Deleting a tuple
# del a  # Uncommenting this line will delete the tuple 'a'
b = a.count(1)
print("Count of 1 in a:", b)
