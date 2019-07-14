from functools import reduce

def squareOfSum(num1, num2):
  return num1 + num2

def sumOfSquare(num1, num2):
  return num1 + (num2 ** 2)

def main():
  print((reduce(squareOfSum, range(1, 100+1, 1)) ** 2) - reduce(sumOfSquare, range(1, 100+1, 1)))


if __name__ == '__main__':
  main()