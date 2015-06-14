# Perceptron con data de get_data

# Full path to your django project directory
django_path = "/Users/jje-personal/projects/facultad/fiuba-robots/Alibaba"

import sys,os
sys.path.append(django_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Alibaba.settings'

from sklearn.linear_model import Perceptron
from utils import get_data
from sklearn import metrics
from time import time

X_train, y_train, X_test, y_test = get_data()
clf = Perceptron()

print('_' * 80)
print("Training: ")
print(clf)
print("Training data lenght: %s" % len(X_train))
print("Test data lenght: %s" % len(X_test))
print('_' * 80)
t0 = time()
clf.fit(X_train, y_train)
train_time = time() - t0
print("train time: %0.3fs" % train_time)

t0 = time()
pred = clf.predict(X_test)
test_time = time() - t0
print("test time:  %0.3fs" % test_time)

score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.3f" % score)

categories=['no', 'si']
print('_' * 80)
print("classification report:")
print(metrics.classification_report(y_test, pred,
                                    target_names=categories))
