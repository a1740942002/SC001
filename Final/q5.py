NUM_ROLLS = 15

import random

def main():
  # init data
  dice_points = ''
  number_of_runs = 0

  for i in range(NUM_ROLLS):
    round = i + 1
    dice_num = random.randrange(1,7)
    dice_points += str(dice_num)
    print('Rolls: ' + str(dice_num))

  last_round_dice_point = ''
  is_switch_round = False
  has_count = False

  for i in range(len(dice_points)):
    dice_point = dice_points[i]
    if last_round_dice_point == '':
      last_round_dice_point = dice_point
    else:
      last_round_dice_point = dice_points[i - 1]
      is_switch_round = last_round_dice_point != dice_point

      if is_switch_round:
        has_count = False

      elif not is_switch_round and not has_count:
        number_of_runs += 1
        has_count = True
        
  print('Number of runs: ' + str(number_of_runs))




if __name__ == "__main__":
  main()


