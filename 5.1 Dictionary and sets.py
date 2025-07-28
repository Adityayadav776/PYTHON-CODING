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

print(marks.get("aditya1"))  #print None if key not found
# print(marks.get("Aditya1", "Key not found"))  #print default message if key not found
print(marks["aditya1"])  #returns KeyError if key not found


#################################################################################################
#SETS
#Sets are unordered collections of unique elements.
#They are mutable and do not allow duplicate values.
#d={} #empty dictionary
s={1, 2, 3, 4, 5}  #set with unique elements
#s=set() #empty set
students = {"Aditya", "Ravi", "Ashutosh", "Sakshi"}
print("Students in the set:", students, "\n", type(students))
#Adding elements to the set
students.add("Anjali")
#Removing elements from the set
students.remove("Ravi")
#Checking if an element exists in the set
if "Aditya" in students:
    print("Aditya is in the set of students.")
#Iterating through the set
for student in students:
    print(f"{student} is a student.")
#Converting a list to a set to remove duplicates
marks_list = [85, 90, 85, 95, 100, 90]
marks_set = set(marks_list)
print("Unique marks are:", marks_set)
#Converting a set to a list
unique_marks_list = list(marks_set)
s.add(105)  # Adding a new element to the set.
#sets are unindexed, so we cannot access elements by index.


