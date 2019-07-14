def check(num):
  for i in range(2, num):
    if (num % i == 0):
      return False
  return True

def main():
  inc = 0
  pNum = 2
  while inc < 10001:
    if (check(pNum)):
      inc += 1
    pNum+=1
  print(pNum - 1)
      

if __name__ == '__main__':
  main()