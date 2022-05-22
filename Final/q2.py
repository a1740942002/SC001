def main():
  a = 1
  b = 2
  print('Answer1: ' + str(a+1))
  print('Answer2: ' + str(a))
  c = stancode(a,b)

  if c:
    print('Answer3: ' + str(a))
  else:
    print('Answer4: ' + str(a))



def stancode(a,b):
  a = b
  b = a
  print('Answer5: ' + str(a+b))
  return a == b


if __name__ == "__main__":
  main()