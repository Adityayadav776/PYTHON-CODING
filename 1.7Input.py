#INPUT Function
Number1= input("Enter number1:")
Number2= input("Enter number2:")
Number3= int(input("Enter number3:"))
Number4= int(input("Enter number4:"))
print("By default it will treat numbers as a string concatenating them:",Number1+Number2) #Python take input as string by default thus it will concatinate the two strings
#Either convert the numbers to int at the of addition or at the time of taking input
print("Sum:", int(Number1) + int(Number2))  # Convert to int for addition
print("Sum of number3 and number4:", Number3 + Number4)  # Directly using int inputs
