"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    #raise valueerror if 0 or <0
    if number_of_primes < 1:
        raise ValueError("Input value can't be less than 1")

    list = []
    num_counter = 2 #1 isn't prime

    while len(list) != number_of_primes:
        for i in range(2, num_counter):
            if num_counter % i == 0:
                break
        else:
            list.append(num_counter)
        num_counter += 1

         
    return list
