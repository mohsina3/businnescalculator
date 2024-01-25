
## Alizeh Mohsin and Harshini Malarvannan
import math
def basic_calculator():
    # Calculates basic mathematical operations


    while True:
        print()
        print("Basic Calculator Operations")
        print("1. Addition(+)")
        print("2. Subtraction(-)")
        print("3. Multiplication(*)")
        print("4. Division(/)")
        print("5. Modulus(mod)")
        print("6. Exponents(^)") 
        print("7. Exit")

        choice = input("Choose the operation you would like to do based on the correlating number: ")

        if choice == "7":
            break       # Exits loop choice is 7
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if choice == "1":
            result = number1 + number2     
            print(result)
        elif choice == "2":
            result = number1 - number2    
            print(result)
        elif choice == "3":
            result = number1 * number2
            print(result)
        elif choice == "4":
            result = number1 / number2 if number2 !=0 else 'error'
            print(result)
        elif choice == "5":
            result = number1 % number2
            print(result)
        elif choice == "6":
            result = number1 ** number2 
            print(result)
        else:
            print('Error, please pick a number 1-7')

    


# Engineering Calculator 
            # Provides calculations for shapes and unit conversions
def engineering_calculator():
    while True:
        print("Engineering Calculations")
        print("1. Calculate Shape")
        print("2. Unit Conversion")
        print("3. Exit")
        print()

        choice = input ("Enter Choice: ")
        if choice == '1':
            return shape_calculation()
        elif choice == '2':
            return unit_conversion()
        elif choice == "3":
            break
        else:
            print("Error, please pick 1, 2, or 3")


def shape_calculation():
    while True:
        shape = input("Enter the shape (options: triangle, rectangle, circle, cube, cylinder, or cone): ")
        print()
        if shape == 'triangle':
            base = float(input("Enter base value of triangle: "))
            height = float(input("Height value of triangle: "))
            length = float(input("Length of triangle: "))
            return {'area': 0.5 * base * height, 'volume': 0.5 * base * height * length}
        
        elif shape == 'rectangle':
            length = float(input("Length of rectangle: "))
            height = float(input("Height value of rectangle: "))
            width = float(input("Width of rectangle: "))
            return {'area': length * width, 'volume':length * width * height}
        
        elif shape == 'circle':
            radius = float(input("Radius of circle: "))
            return {'area':math.pi * (radius ** 2), 'volume': 4/3 * math.pi * (radius ** 3)}
        
        elif shape == 'cube':
            edge = float(input("Edge of cube: "))
            return {'area': 6 * (edge ** 2), 'volume':(edge**3)}
        
        elif shape == 'cylinder':
            radius = float(input("Radius of cylinder: "))
            height = float(input("Height value of cylinder: "))
            return {'area':2 * math.pi * radius (radius + height), 'volume': math.pi * (radius ** 2) * height}
        
        elif shape == 'cone':
            radius = float(input("Radius of cone: "))
            height = float(input("Height value of cone: "))
            slHeight = float(input("Slant height of cone: "))
            return {'area':math.pi* (radius**2) + (math.pi*radius *slHeight), 'volume':1/3 * math.pi * (radius ** 2) * height}
        else:
            return 'Error, plase pick from the menu of shape options, also check for spelling errors'
def unit_conversion():
    while True:
        unit = input("Do you want to convert from meters_to_feet OR kilograms_to_pounds? ")
        value = float(input("Value to convert: "))
        if unit == "meters_to_feet":
            result = value * 3.28084
            print(f"{value} meters is equal to {result} feet")
        elif unit == "kilograms_to_pounds":
            result = value * 2.20462
            print(f"{value} kilograms is equal to {result} pounds")
        else:
            print("invalid, please enter 'meters_to_feet' OR 'kilograms_to_pounds'")

    
def business_calc():
   #    Calculate the compound interest for a given principal amount

    while True:
        print("Choose one of the following:")
        print("1: Compound Interest")
        print("2: Break-Even Point")
        print("3: Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            prin_amt = int(input("Enter a principal amount: "))
            i = float(input("Enter the annual interest rate in decimal (if 15%, enter 0.15): "))
            n = int(input("Enter the number of periods: "))

            answer = float(((prin_amt * (1+i)**n)-prin_amt))
            print(answer)

        elif choice == "2":
            
                f = float(input("Enter the fixed costs: "))
                v = float(input("Enter the variable costs per unit: "))
                s = float(input("Enter the selling price per unit: "))

                if (s-v) == 0:                                                                          ## checking for computation error with dividing by zero
                    print("Error! Vairable cost and selling price cannot be the same.")
                    
                else:
                    ans = f / (s-v)
                    print(ans)

        elif choice == "3":
            break
        else:
            print("Invalid. Please enter a number between 1 and 3.")



def main_menu():
    while True:
        print("Main Menu")
        print("1. Basic Calculator")
        print ("2. Engineering Calculator")
        print ("3. Business Calculator")
        print ("4. Exit")
        print()   ##new line for user-friendly looks

        choice = input("Enter the number that corresponds with the calculator you want to use: ")
        print()
        if choice == '1':
            print("Result:", basic_calculator())
        elif choice == '2':
            print (engineering_calculator())
            print()
        elif choice == '3':
            print("Result:", business_calc())
        elif choice == '4':
            break
        else:
            print('invalid, please pick a number corresponding to our menu options')

main_menu()



    




