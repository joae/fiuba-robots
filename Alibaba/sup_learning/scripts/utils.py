from sup_learning.models import SubmissionTest, SubmissionTrain
from sklearn.cross_validation import train_test_split
import numpy as np

def get_data():
	'''
	Levanta la data tal cual la metimos en la DB
	'''
	all_train = SubmissionTrain.objects.all()
	all_test = SubmissionTest.objects.all()

	X_train = [[entry.user_id, entry.merchant_id, entry.age_range, entry.gender] for entry in all_train]
	X_train = np.array(X_train)
	y_train = [entry.prob for entry in all_train]

	X_test = [[entry.user_id, entry.merchant_id, entry.age_range, entry.gender] for entry in all_test]
	X_test = np.array(X_test)
	y_test = [entry.prob for entry in all_test]

	return X_train, y_train, X_test, y_test

def get_data2(test_size=0.25):
	'''
	Arma el set de datos seleccionando de manera random con
	Set de entrenamiento de 1 - test_size %. Default 0.75
	Set de test de test_size %. Default 0.25  
	'''
	all_train = SubmissionTrain.objects.all()
	all_test = SubmissionTest.objects.all()

	X_train = [[entry.user_id, entry.merchant_id, entry.age_range, entry.gender] for entry in all_train]
	X_train = np.array(X_train)
	y_train = [entry.prob for entry in all_train]

	X_test = [[entry.user_id, entry.merchant_id, entry.age_range, entry.gender] for entry in all_test]
	X_test = np.array(X_test)
	y_test = [entry.prob for entry in all_test]

	X = np.concatenate((X_train, X_test), axis=0)
	y = np.concatenate((y_train, y_test), axis=0)
	rng = np.random.RandomState(42)
	X_train, X_test, y_train, y_test = \
                train_test_split(X, y, test_size=test_size, random_state=rng)

	return X_train, y_train, X_test, y_test