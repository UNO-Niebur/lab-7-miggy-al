""" Loop through products of 3 digit numbers and checks if it is palindrome 
   and keeps the largest one found """
#Problem4.py
#Project Euler problem 4
from NumberTests import isPalindrome

def main():
    
    large_p = 0
    for i in range(1000, 100, -1):
       for j in range(i, 100, -1):
          product = i * j
          if isPalindrome(product):
             if product > large_p:
                large_p = product
    print("The largest palindrome made from the product of 2 same 3-digit numbers is:"
          , large_p)
    
if __name__ == '__main__':
  main()