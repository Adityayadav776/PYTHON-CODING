#Write a program to print the contents of a directory using the os module. Search for the function which does that.
import os

# Select directory path you want to list
# Ensure the path is correct and accessible
directory_path = "\\old Window"

# Get the list of files and folders of this directory
# Using os.listdir() to list the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)

#Make new directory and print directory
os.mkdir("D:\\S\\New Folder")
# Print confirmation of directory creation
print("New Directory Created: New Folder in D:\\S\\")