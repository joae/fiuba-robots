# Perceptron con data de get_data

# Full path to your django project directory
django_path = "/Users/jje-personal/projects/facultad/fiuba-robots/Alibaba"

import sys,os
sys.path.append(django_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Alibaba.settings'

from sklearn.linear_model import Perceptron
from utils import get_data2
from sklearn import metrics
from time import time
import numpy as np
import matplotlib.pyplot as plt

heldout = [0.95, 0.90, 0.75, 0.50, 0.01]

classifiers = [
	('iter:5', Perceptron(n_iter=5)),
	('iter:10', Perceptron(n_iter=10)),
	('iter:100', Perceptron(n_iter=100)),
	('iter:1000', Perceptron(n_iter=1000)),
	('iter:3000', Perceptron(n_iter=3000))
]

xx = 1. - np.array(heldout)

for name, clf in classifiers:
	yy = []
	for size in heldout:
		X_train, y_train, X_test, y_test = get_data2(size)
		t0 = time()
		clf.fit(X_train, y_train)
		train_time = time() - t0
		print("%s: train time: %0.3fs" % (name, train_time))

		t0 = time()
		y_pred = clf.predict(X_test)
		test_time = time() - t0
		print("%s: test time:  %0.3fs" % (name, test_time))
		# yy.append(1 - np.mean(y_pred == y_test))
		yy.append(metrics.accuracy_score(y_test, y_pred))
	plt.plot(xx, yy, label=name)

plt.legend(loc="upper right")
plt.xlabel("Proportion train")
plt.ylabel("Test Error Rate")
plt.show()
