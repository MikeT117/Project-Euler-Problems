def main():
  s, c = 1000, 0

  for i in range(1, int(s/3), 1):
    for j in range(1, int(s/2), 1):
      c = s - i - j
      if ((i**2)+(j**2) == c **2):
        print (f"Product: ",i * j * c)

if __name__ == '__main__':
  main()