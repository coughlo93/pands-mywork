# collatz.py

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    try:
        # Get a positive integer from the user
        num = int(input("Please enter a positive integer: "))
        if num <= 0:
            raise ValueError("Please enter a positive integer.")
        
        # Generate and print the Collatz sequence
        sequence = collatz_sequence(num)
        print(" ".join(map(str, sequence)))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
