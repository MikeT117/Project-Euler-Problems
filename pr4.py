def check(val):
  lenHlv = len(str(val)) // 2
  arr1, arr2 = list(map(int, str(val)))[:lenHlv], list(map(int, str(val)))[lenHlv:]

  if arr1==arr2[::-1]:
      return True

def main():
  currVal = 0
  for i in range(100, 999, 1):
    for j in range(100, 999, 1):
      if (len(str(i*j)) % 2 == 0 and (check(i*j))):
        if (i*j > currVal):
          currVal = i*j
  print(currVal)
if __name__ == '__main__':
  main()