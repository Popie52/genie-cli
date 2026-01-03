
# add.py - A verbose Python script for adding three numbers

import sys

def add_numbers(num1, num2, num3):
    """
    This function takes three numbers as input and returns their sum.
    It also prints verbose messages about the operation.
    """
    print(f"DEBUG: Entering add_numbers function with num1={num1}, num2={num2}, and num3={num3}")
    
    # Performing the addition
    result = num1 + num2 + num3
    
    print(f"DEBUG: Calculation performed: {num1} + {num2} + {num3} = {result}")
    
    return result

def main():
    print("INFO: Starting the add.py script.")
    
    # Check if exactly three arguments (numbers) are provided
    if len(sys.argv) != 4:
        print("ERROR: Incorrect number of arguments provided.")
        print("USAGE: python add.py <number1> <number2> <number3>")
        print("EXAMPLE: python add.py 5 10 15")
        sys.exit(1) # Exit with an error code
        
    try:
        # Attempt to convert command-line arguments to floats
        print(f"INFO: Attempting to convert arguments '{sys.argv[1]}', '{sys.argv[2]}' and '{sys.argv[3]}' to numbers.")
        number1 = float(sys.argv[1])
        number2 = float(sys.argv[2])
        number3 = float(sys.argv[3])
        print(f"INFO: Successfully converted arguments to number1={number1}, number2={number2}, number3={number3}")
        
        # Call the function to add the numbers
        print("INFO: Calling add_numbers function to perform addition.")
        sum_result = add_numbers(number1, number2, number3)
        
        # Print the final result in a verbose manner
        print("\nRESULT: The sum of {0}, {1} and {2} is: {3}".format(number1, number2, number3, sum_result))
        print("INFO: Script finished successfully.")
        
    except ValueError:
        print("ERROR: Invalid input. Please ensure all arguments are valid numbers.")
        print("USAGE: python add.py <number1> <number2> <number3>")
        sys.exit(1) # Exit with an error code

if __name__ == "__main__":
    main()
