def main(): 
  mainVal = 600851475143
  div = 2
  while True:
    while not ((mainVal / div).is_integer()):
      div +=1
    while ((mainVal / div).is_integer()):
      mainVal = mainVal / div
      print (div)
      if (mainVal == 1):
        exit()

if __name__ == '__main__':
  main()