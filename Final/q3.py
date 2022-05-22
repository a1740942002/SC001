def main():
  name_diamond('JENNIFER')


def name_diamond(name):
  length = len(name) - 1

  for i in range(length):
    blank_count = length - i
    print(name[:i+1], end="")
    for j in range(blank_count):
      print(" ", end="")
    print('')

  print(name)

  for i in range(length):
    blank_count = i + 1
    for j in range(blank_count):
      print(" ", end="")
    print(name[i + 1:len(name)], end="")
    print('')


if __name__ == "__main__":
  main()


