#Declare static variables
import sys

PI = 3.14159
i = 0 #Used in the MAIN while loop
# **** FUNCTIONS ****

#Function: Invalid input from user
def invalid_input():
    print("\nInvalid option. Please try again.\n")
    input("Press Enter to continue...\n")

#Function for Area of Square
def area_square(width):
    print (width * width)

#Function for Area of Circle
def area_circle(radius):
    print (PI * (radius * radius) )

#Function: Convert int to string
def convert_to_string(x):
    return str(x)

#Function: Reverse string 
def reverse_string(x):
  return x[::-1]

#Function: Display Palindromes
def palindrome():
    #Loop through numbers 1-999
    for i in range(1000):
        x = convert_to_string(i) #Convert from integer to string data type
        y = reverse_string(x)   #Use the reverse_string python function
        #check if the number is a palindrome
        if x == y:
            print(x)

#Function: Display menu
def display_menu():
    print("Calculations")
    print("1. Calculate area of a square")
    print("2. Calculate area of a circle")
    print("3. Display palindromes up to 1,000")
    print("4. Exit")

#Function: Get user input for menu option
def user_input():
    x = int(input("Enter an option: "))
    return x

#Function: Make sure userinput option is between 1-4
#If selection is between 1-4, perform the appropriate function
def menu_options(user_selection):
    #if user_selection >= 1 and user_selection <= 4:
    if user_selection == 1:
        #Call area square function
        width = int(input("Please enter the width of a square: "))
        area_square(width)
    elif user_selection == 2:
        #Call area circle function
        radius = int(input("Please enter the radius of the circle: "))
        area_circle(radius)
    elif user_selection == 3:
        #Call palindrome function
        palindrome()
    else:
        print("Goodbye!!!")
        sys.exit(0)

#   **** MAIN ****
while i < 1: #While loop to prompt the user to choose an option until they exit 
    try:
        display_menu()
        user_selection = user_input()
        menu_options(user_selection)
        input("\nPress Enter to continue...\n")
    except Exception:
        invalid_input()
