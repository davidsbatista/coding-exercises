__author__ = 'dsbatista'


def prime_numbers(n):
    primes = list()
    for i in range(0, n+1):
        # Any even number is not prime.
        if i % 2 == 0:
            continue

        prime = True
        # A number is prime if it is not divisible by any previous primes.
        for x in primes[1:]:
            if i % x == 0:
                prime = False
                break

        if prime is True:
            primes.append(i)

    return primes


def main():
    print prime_numbers(50000)

if __name__ == "__main__":
    main()