def check(num):
  for i in range(2, int(num ** 0.5) + 1, 1):
    if (num % i == 0):
      return False
  return True

def main(num = 2000000):
  pList = []
  for i in range(2, num, 1):
    if (check(i)):
      pList.append(i)

  print(sum(pList))
      

if __name__ == '__main__':
  main()