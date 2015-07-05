'''
Compara distintos metodos variando el porcentaje que usa para entrenar
Cantidad de datos: TODOS (los que se hayan insertado en la DB)
test/train: variable

Grafica: (por cada clasificador definido)
- accuracy_score vs proportion train

'''
# Full path to your django project directory
django_path = "/home/joa/Documents/Facultad/robots/fiuba-robots/Alibaba"

import sys,os
sys.path.append(django_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Alibaba.settings'

from sklearn.linear_model import Perceptron
from utils import get_data2
from sklearn import metrics
from time import time
import numpy as np
import matplotlib.pyplot as plt
from sup_learning.mlp.multilayer_perceptron import MLPClassifier

categories=['no', 'si']

heldout = [0.95, 0.90, 0.75, 0.50, 0.01]

classifiers = [
	# ('iter:5', Perceptron(n_iter=5)),
	('iter:10', Perceptron(n_iter=10)),
	('iter:100', Perceptron(n_iter=100)),
	# ('iter:1000', Perceptron(n_iter=1000)),
	# ('iter:3000', Perceptron(n_iter=3000)),
	# ('MLP:hidden:1', MLPClassifier(hidden_layer_sizes=(1,))),
	# ('MLP:hidden:2', MLPClassifier(hidden_layer_sizes=(2,))),
	('MLP:hidden:5', MLPClassifier(hidden_layer_sizes=(5,))),
	('MLP:hidden:10', MLPClassifier(hidden_layer_sizes=(10,))),
	('MLP:hidden:50', MLPClassifier(hidden_layer_sizes=(50,)))
]

xx = 1. - np.array(heldout)

for name, clf in classifiers:
	yy = []
	for size in heldout:
		X_train, y_train, X_test, y_test = get_data2(size)

		t0 = time()
		clf.fit(X_train, y_train)
		train_time = time() - t0

		t0 = time()
		y_pred = clf.predict(X_test)
		test_time = time() - t0

		print('_' * 80)
		print("\nclassification report for %s"%name)
		print("train time: %0.3fs" % train_time)
		print("test time:  %0.3fs" % test_time)
		print(metrics.classification_report(y_test, y_pred,
	                                    target_names=categories))
		print('precision %s' % metrics.precision_score(y_test, y_pred))

		yy.append(metrics.accuracy_score(y_test, y_pred))

	plt.plot(xx, yy, label=name)

plt.legend(loc="upper right")
plt.xlabel("Proportion train")
plt.ylabel("Rate error")
plt.show()
