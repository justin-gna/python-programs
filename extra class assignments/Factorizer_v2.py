# Justin G.
# 2/16/2021
# Number Factorizer Program

# Modulos Operator, 1D lists, Loops

def calc_factors(number):
  factors = []
  for i in range(1, number + 1):
    # if i divides evenly into num
    if number % i == 0:
      factors.append(i)

  return factors

def calc_primes(number):
  primes = []
  factors = calc_factors(number)
  for i in factors:
    # if only has two factors then it is prime
    if len(calc_factors(i)) == 2:
      primes.append(i)
  
  return primes

def calc_prime_factors(number):
  prime_factors = []
  primes = calc_primes(number)
  for i in primes:
    # divides the number by its first prime which will always work
    remainder = number % i
    answer = number / i 
    prime_factors.append(i)
    repeat = True

    # while loop to continue dividing until the prime no longer goes into the next answer evenly or until the answer == 1 
    while repeat == True:
      remainder = answer % i
      answer = answer / i 
      if remainder == 0 or answer == 1:
        repeat = True
        prime_factors.append(i)
      else:
        repeat = False

  return prime_factors


num = int(input("enter a number to factorize: "))

factors = calc_factors(num)
primes = calc_primes(num)
prime_factors = calc_prime_factors(num)

print("factors:", factors)
print("primes:", primes)
print("prime factors:", prime_factors)
