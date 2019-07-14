def main(): 
  val = 0

  for i in range(1000): 
    if i % 3 == 0 or i % 5 == 0:
      val += i

  print(val)
    
if __name__ == '__main__':
  main()