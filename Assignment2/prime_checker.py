"""
File: prime_checker.py
Name: Brian Lai
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
  """
  TODO:
  Ask user to input a int number and keep telling them whether this number is a prime or not.
  If user want to leave, they just need to input '-100', then they can exit this program.
  """
  print("Welcome to the prime checker!")

  while True:
    n = int(input('n: '))
    if n == EXIT:
      print('Have a good one!')
      break

    if is_prime(n):
      print(str(n) + ' is a prime number.')
    else:
      print(str(n) + ' is not a prime number.')


def is_prime(n):
  """
  Returns a Boolean result whether int 'n' is a prime number.

  :param n: int, a int number.
  """
  for i in range(n):
    # A prime number is that only 1 and itself could divide it without getting any decimal number.
    # so we should compare from 2 to n - 1
    if i == 0 or i == 1 or i == n:
      pass
    elif n % i == 0:
      return False
    
  return True


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
