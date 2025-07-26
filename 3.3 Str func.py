#string functions
a="application for the testing"
print(len(a))
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.count('c'))
print(a.find('t'))
print(a.replace('app', 'du'))
print(a.startswith('ca'))
print(a.endswith('io'))
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(a.islower())
print(a.isupper())
print(a.isnumeric())
print(a.split('a'))  # Splits the string at 'a' and returns a list
print(a.split())  # Splits the string at whitespace and returns a list
print(a.strip())  # Removes leading and trailing whitespace
print(a.lstrip())  # Removes leading whitespace
print(a.rstrip())  # Removes trailing whitespace
print(a.index('c'))  # Returns the index of the first occurrence of 'c'
print(a[2:5])  # Slicing the string from index 2 to 5 (exclusive)
print(a[-3:])  # Slicing the last three characters of the string
print(a[1:])  # Slicing from index 1 to the end of the string
print(a[::-1])  # Reverses the string
print(a[::2])  # Slicing the string with a step of 2
print(a[1:10:2])  # Slicing from index 1 to 10 with a step of 2
print(a[1:])  # Slicing from index 1 to the end of the string
print(a[-1])  # Accessing the last character of the string.
