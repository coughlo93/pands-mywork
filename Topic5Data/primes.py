# generate primes
# Author: Owen Coughlan

primes = []
upto = 1001

for candidate in range(2, upto):
     #print (candidate)
    isPrime = True
    # only need to check if divisible by prim
    for divisor in primes:
            # if divisible by an int it is not a prime number
            if (candidate % divisor == 0):
                isPrime = False
                # so there is not a reason to keep checking
                break
            
    if isPrime:
        primes.append(candidate)

print(primes)