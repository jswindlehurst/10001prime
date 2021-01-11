
# returns True if parameter n is a prime number, False if composite and "Neither prime, nor composite" if neither

def prime_num(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n//2) + 1):
        if n % i == 0:
            return False
    return True

def find_prime(n):
    number_primes = 0
    prime = 1

    while number_primes < n:
        prime += 1
        if prime_num(prime):
            number_primes += 1
    return prime


def main():

    # returns the chosen prime number

    print(find_prime(10001))

if __name__ == '__main__':
        main()