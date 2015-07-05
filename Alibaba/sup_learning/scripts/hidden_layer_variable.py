'''
Compara distinta cantidad de capas ocultas definidas en sizes
Cantidad de datos: 10000
test/train: 70/30

Grafica:
- precision vs hidden_layer_sizes
- rate error vs hidden_layer_sizes
'''
# Full path to your django project directory
django_path = "/home/joa/Documents/Facultad/robots/fiuba-robots/Alibaba"

import sys,os
sys.path.append(django_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Alibaba.settings'

from sklearn.linear_model import Perceptron
from utils import get_data
from sklearn import metrics
from time import time
import numpy as np
import matplotlib.pyplot as plt
# from sklearn.neural_network.multilayer_perceptron import MLPClassifier
from sup_learning.mlp.multilayer_perceptron import MLPClassifier

sizes = [1, 2, 10, 20, 50, 75, 100]

classifiers = [
	('MLP:hidden:1', MLPClassifier(hidden_layer_sizes=(1,))),
	('MLP:hidden:2', MLPClassifier(hidden_layer_sizes=(2,))),
	('MLP:hidden:10', MLPClassifier(hidden_layer_sizes=(10,))),
	('MLP:hidden:20', MLPClassifier(hidden_layer_sizes=(20,))),
	('MLP:hidden:50', MLPClassifier(hidden_layer_sizes=(50,))),
	('MLP:hidden:75', MLPClassifier(hidden_layer_sizes=(75,))),
	('MLP:hidden:100', MLPClassifier(hidden_layer_sizes=(100,))),
]

X_train, y_train, X_test, y_test = get_data()

categories=['no', 'si']
print('_' * 80)
print("classification report:")

xx = np.array(sizes)
yy = []
ee = []
for name, clf in classifiers:

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
	yy.append(metrics.precision_score(y_test, y_pred))
	ee.append(metrics.accuracy_score(y_test, y_pred))

plt.plot(xx, yy, label='precision')
plt.plot(xx, ee, label='error')

plt.legend(loc="upper right")
plt.title("10000 datos - 70train/30test")
plt.xlabel("Hidden Layers")
plt.ylabel("Precision score")
plt.show()


