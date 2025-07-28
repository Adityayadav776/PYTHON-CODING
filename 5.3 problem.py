#Take input of 5 name and language pairs and store them in a set.

s={}
for i in range(5):
    while True:
        try:
            name=input("Enter name:")
            language=input("Enter language:")
            if not name or not language:
                raise ValueError("Name and Language can't be empty")
            s.update({name: language})
            break
        except ValueError as e:
            print("Invalid Input. Please try again",e)
print("Name and Language Pairs are:",s)
        