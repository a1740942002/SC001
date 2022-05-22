###########################
# import matplotlib       #
# matplotlib.use('TKAgg') #
###########################
import pandas as pd
import matplotlib.pyplot as plt


def main():
	file_path = './titanic_data/train.csv'
	data = pd.read_csv(file_path)
	print(data.head())
	print(data.count())

	plt.figure(figsize = (18,7))
	###############################################

	# Row1
	plt.subplot2grid((3,4),(0,0))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind = 'bar', color='blue')
	plt.title('Survived')

	plt.subplot2grid((3,4),(0,1))
	data.Sex.value_counts(normalize=True).sort_index().plot(kind = 'bar', color="brown")
	plt.title('Sex')

	plt.subplot2grid((3,4),(0,2))
	data.Pclass.value_counts(normalize=True).sort_index().plot(kind = 'bar', color="purple")
	plt.title('Pclass')

	# Row 2
	plt.subplot2grid((3,4), (1,0))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='magenta')
	plt.title('Man Survived')

	plt.subplot2grid((3,4), (1,1))
	data.Survived[data.Sex == 'female'].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Woman Survived')

	plt.subplot2grid((3,4), (1,2))
	data.Survived[data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Pclass1 Survived')

	plt.subplot2grid((3,4), (1,3))
	data.Survived[data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Pclass3 Survived')

	# Row 3
	plt.subplot2grid((3,4), (2, 0))
	data.Survived[(data.Sex == 'male')&(data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(kind='bar', color='magenta')
	plt.title('Rich Man Survived')

	plt.subplot2grid((3,4), (2, 1))
	data.Survived[(data.Sex == 'male')&(data.Pclass == 3)].value_counts(normalize=True).sort_index().plot(kind='bar', color='magenta')
	plt.title('Poor Man Survived')

	plt.subplot2grid((3,4), (2, 2))
	data.Survived[(data.Sex == 'female')&(data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Rich Woman Survived')

	plt.subplot2grid((3,4), (2, 3))
	data.Survived[(data.Sex == 'female')&(data.Pclass == 3)].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Poor Woman Survived')


	###############################################
	plt.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
