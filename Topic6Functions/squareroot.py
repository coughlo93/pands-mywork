def sqrt(number):
    # Initial guess (you can choose any positive number)
    guess = number / 2.0
    
    # The precision of the result
    epsilon = 0.00001
    
    # Newton-Raphson method for approximating square root
    while abs(guess * guess - number) > epsilon:
        guess = (guess + number / guess) / 2.0
    
    return guess

if __name__ == "__main__":
    try:
        # Get user input
        number = float(input("Please enter a positive number: "))
        
        # Check if the number is positive
        if number < 0:
            print("Please enter a positive number.")
        else:
            # Calculate and display the square root approximation
            result = sqrt(number)
            print(f"The square root of {number} is approx. {result:.2f}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid positive number.")
