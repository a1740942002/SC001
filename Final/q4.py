def main():
  # init data
  max = -1
  min = -1
  avg = 0
  total = 0
  valid_data_count = 0
  file_path = './data.txt'

  with open(file_path, "r") as f:
    for line in f:
      is_Nan = line.find('.') == -1
      
      if is_Nan:
        pass
      else:
        data = float(line)

        is_first_data = max == -1 and min == -1
        if is_first_data:
          max = data
          min = data

        valid_data_count += 1
        total += data

        if data >= max:
          max = data
        
        if data <= min:
          min = data

  if valid_data_count > 0:
    avg = total / valid_data_count
    print('Max: ' + str(max))
    print('Min: ' + str(min))
    print('Avg: ' + str(avg))
  else:
    print('No data in this file')




if __name__ == "__main__":
  main()


