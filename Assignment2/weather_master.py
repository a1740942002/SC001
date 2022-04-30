"""
File: weather_master.py
Name: Brian Lai
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100

def main():
	"""
	TODO: Ask user to input a integar, calculate and display the result when user decide to leave.
	"""
	print('stanCode "Weather Master 4.0"!')

	# Init Data
	highest_temperature = 0
	lowest_temperature = 0
	total_temperature = 0
	input_count = 0
	average = 0
	cold_day_count = 0 

	# First Input
	temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	
	# Computed Data
	highest_temperature = temperature
	lowest_temperature = temperature
	total_temperature = temperature
	input_count += 1
	average = get_average(total_temperature, input_count)
	if is_cold_day(temperature):
		cold_day_count += 1


	while True:
		# If first time input EXIT, then EXIT without printing result.
		if input_count == 1 and temperature == EXIT:
			print('No temperatures were entered.')
			break

		new_temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))

		# When user input EXIT, then print result.
		if new_temperature == EXIT:
			print('Highest temperature = ' + str(highest_temperature))
			print('Lowest temperature = ' + str(lowest_temperature))
			print('Average = ' + str(average))
			print(str(cold_day_count) + ' cold day(s)')
			break
		
		# Update next round Data
		highest_temperature = get_higher_number(highest_temperature, new_temperature)
		lowest_temperature = get_lower_number(lowest_temperature, new_temperature)
		total_temperature += new_temperature
		input_count += 1
		average = get_average(total_temperature, input_count)
		if is_cold_day(new_temperature):
			cold_day_count += 1
		temperature = new_temperature

	

def get_average(total, count):
	"""
	Given total number count, return its average (float).

	:params total: int
	:params count: int
	"""
	return float(total / count)


def is_cold_day(temperature):
	"""
	Given 1 temperature, return whether is cold day (boolean).

	:param temperature: int
	"""
	if temperature <= 16:
		return True
	return False


def get_higher_number(number_1, number_2):
	"""
	Given 2 int, return higher one (int).

	:params number_1: int
	:params number_2: int
	"""
	if number_1 >= number_2:
		return number_1
	else:
		return number_2


def get_lower_number(number_1, number_2):
	"""
	Given 2 int, return lower one (int).

	:params number_1: int
	:params number_2: int
	"""

	if number_1 <= number_2:
		return number_1
	else:
		return number_2


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
