#Modular approach to each action of the calculator
def add(x, y,):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("You cannot divide by zero!")

#A simple CLI interface to get inputs from the user and perform calculations using the main function 
def main():
    options = ["Add", "Subtract", "Multiply", "Divide", "Exit"]

    while True:        
        print("Welcome to the Calculator app! Please select from the following options: \n")
        
        for i, option in enumerate(options, 1):
            print(f"{i} - {option}")
        
        try:
            feature = int(input("\nEnter you choice from 1-5: "))
            if feature == 5:
                print("You have chosen to exit the app!")
                break
            elif 1 <= feature <= 4:
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))

                if feature == 1:
                    print(f"The sum is: {add(x, y)}\n")
                elif feature == 2:
                    print(f"The difference is: {sub(x, y)}\n")
                elif feature == 3:
                    print(f"The multiplied result is: {multiply(x, y)}\n")
                elif feature == 4: 
                    print(f"The divided result is: {divide(x, y)}\n")   
            else:
                print("You have chosen to exit the app!\n")
        except ValueError:
            print("Invalid input! Please enter only integer values from 1-5\n")

            
if __name__ == "__main__":
    main()