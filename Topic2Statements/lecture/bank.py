def main():
  """
  Prompts user for two amounts, adds them, and prints the sum in euro format.
  """
  amount1 = int(input("Enter amount1(in cent): "))
  amount2 = int(input("Enter amount2(in cent): "))

  # Calculate the sum and convert it to euros with two decimal places
  sum_euros = (amount1 + amount2) / 100

  # Print the result in euro format
  print(f"The sum of these is €{sum_euros:.2f}")

if __name__ == "__main__":
  main()
