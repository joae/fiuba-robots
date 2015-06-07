
csv_test="/home/giovanni/FIUBA/robots/fiuba-robots/Alibaba/data_format1/test.csv"
csv_train="/home/giovanni/FIUBA/robots/fiuba-robots/Alibaba/data_format1/train.csv"

# Full path to your django project directory
django_path = "/home/giovanni/FIUBA/robots/fiuba-robots/Alibaba/Alibaba/"

import sys,os
sys.path.append(django_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from sup_learning.models import SubmissionTest, SubmissionTrain

import csv
dataReader = csv.reader(open(csv_test), delimiter=',', quotechar='"')

for row in dataReader:
	submission_test = SubmissionTest()
	submission_test.user_id = row[0]
	submission_test.merchant_id = row[1]
	submission_test.prob = row[2]
	submission_test.save()

dataReader = csv.reader(open(csv_train), delimiter=',', quotechar='"')

for row in dataReader:
	submission_train = SubmissionTrain()
	submission_train.user_id = row[0]
	submission_train.merchant_id = row[1]
	submission_train.prob = row[2]
	submission_train.save()	
