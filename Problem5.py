"""Generates all the prime numbers below 2000000 and then using Summation_of_Primes 
and adding them together to get the total sum"""
#Problem5.py
#Project Euler problem 5
from NumberTests import Summation_of_Primes

def main():
 bound = 2000000
 prime_numbers = Summation_of_Primes(bound)
 total_sum = sum(prime_numbers)
 print("Sum of the primes below 2000000 is", total_sum)
   
if __name__ == '__main__':
  main()