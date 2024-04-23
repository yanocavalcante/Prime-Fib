import fibonnaci
import prime

if __name__ == "__main__":
    #Testing fibonnaci functions
    print(fibonnaci.lin_fib(8))
    print(fibonnaci.rec_fib(8))

    #Testing prime numbers functions
    primes_list = []
    print(prime.lin_prime(30))
    print(prime.rec_prime(30, primes_list))