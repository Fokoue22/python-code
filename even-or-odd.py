# Python program to check if the input number is odd or even.

num = int(input("Please enter a number between 1-100: "))
if (num % 2) == 0:
   print(f"{num} is Even") # A number is even if division by 2 gives a remainder of 0.
else:
   print(f"{num} is Odd")  # If the remainder is 1, it is an odd number.