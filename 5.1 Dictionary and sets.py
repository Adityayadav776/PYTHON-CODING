#Dictionary is a collection of key value pairs.
#It is unordered, mutable and indexed.
#Keys must be unique and immutable.

marks = {
    "Aditya": 100,
    "Ravi": 90,
    "Ashutosh": 95,
    "Sakshi": 85,
}
print("Marks of Students are:", marks, "\n",type(marks))
# print(marks.keys())  # Returns keys of the dictionary
# print(marks.values())  # Returns values of the dictionary
# print(marks.items())  # Returns key-value pairs of the dictionary
#Adding a new key-value pair
marks["Anjali"] = 88
#Updating an existing key-value pair
marks["Ravi"] = 92
#Removing a key-value pair
del marks["Ashutosh"]
print("Updated Marks of Students are:", marks)
#Checking if a key exists in the dictionary
if "Aditya" in marks:
    print("Aditya's marks are:", marks["Aditya"])
#Iterating through the dictionary
for student, mark in marks.items():
    print(f"{student} has scored {mark} marks.")