from math import gcd
from functools import reduce

def lcm(num1, num2):  
  return num1*num2//gcd(num1,num2)

def main():
  print(reduce(lcm, range(1, 20)))

if __name__ == '__main__':
  main()