def main(): 
  maxVal = 4000000
  oldVal = 1
  currVal = 1
  rValue = 0

  while currVal <= maxVal:
      currVal, oldVal = currVal + oldVal, currVal
      if currVal % 2 == 0:
        rValue += currVal
  
  print(rValue)

    
if __name__ == '__main__':
  main()