#Declare static variables
PI = 3.14159

# **** FUNCTIONS ****

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
        x = convert_to_string(i)
        y = reverse_string(x)
        #check if the number is a palindrome
        if x == y:
            print(x)

#Function: Display menu
def display_menu():
    print("Calculations")
    print("1. Calculate area of a square")
    print("2. Calculate area of a circle")
    print("3. Display palindromes up to 1,000")

#Function: Get user input for menu option
def user_input():
    x = int(input("Enter an option: "))
    return x

#Function: Make sure userinput option is between 1-3
#If selection is between 1-3, perform the appropriate function
def menu_options(user_selection):
    if user_selection >= 1 and user_selection <= 3:
        if user_selection == 1:
            #Call area square function
            width = int(input("Please enter the width of a square: "))
            area_square(width)
        elif user_selection == 2:
            #Call area circle function
            radius = int(input("Please enter the radius of the circle: "))
            area_circle(radius)
        else:
            #Call palindrome function
            palindrome()
    #User inputs number outside of 1-3 range
    else:
        print("\nInvalid option. Please enter a valid number between 1-3.\n")


#   **** MAIN ****
display_menu()
user_selection = user_input()
menu_options(user_selection)



