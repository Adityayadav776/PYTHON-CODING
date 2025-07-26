#Write a program to detect double space in a string.
str="today's weather is  warm   but not hot yet  feels bright and  cheerful"
for i in range(len(str)-1):
    if str[i:i+2]=="  ":
        print("Double spaces at index:",i)

#Original string dont change as strings are immutable unlike lists in python
# so it prints new string with changes
print(str.replace("  "," "))
print(str)
