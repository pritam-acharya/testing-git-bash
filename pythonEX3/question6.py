primes = [2]
# we start off the list with the smallest prime 2.
# so that we can check the primality of the numbers greater than 2.
NPrimes = input("Please enter the number of Primes you want to see: ")    # NPrimes = Number of Primes.
NPrimes = int(NPrimes)
IniNum = 3                                                                # IniNum = the initial number to run our primality test on, which is 3.
while len(primes) < NPrimes:                                              # limit the length of the list to the first hundred.
    prime = True
    for divisor in primes:
        if IniNum % divisor == 0:
            prime = False
            break
    if prime:
        primes.append(IniNum)

    IniNum = IniNum + 1

print(f"The first {NPrimes} Prime Numbers are")
print(primes)