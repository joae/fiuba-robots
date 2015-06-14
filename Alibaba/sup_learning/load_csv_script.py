
csv_test="data_format1/test.csv"
csv_train="data_format1/train.csv"

# Full path to your django project directory
django_path = "/Users/jje-personal/projects/facultad/fiuba-robots/Alibaba"

import sys,os
sys.path.append(django_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Alibaba.settings'

from sup_learning.models import SubmissionTest, SubmissionTrain

import csv
dataReader = csv.reader(open(csv_test), delimiter=',', quotechar='"')

for row in dataReader:
	submission_test = SubmissionTest()
	submission_test.user_id = row[0]
	submission_test.merchant_id = row[1]
	submission_test.prob = row[2]
	submission_test.age_range = (row[3],0)[row[3]==''] # hack por si no esta la edad
	submission_test.gender = (row[3],0)[row[3]==''] # hack por si no esta el genero
	submission_test.save()

dataReader = csv.reader(open(csv_train), delimiter=',', quotechar='"')

for row in dataReader:
	submission_train = SubmissionTrain()
	submission_train.user_id = row[0]
	submission_train.merchant_id = row[1]
	submission_train.prob = row[2]
	submission_train.age_range = (row[3],0)[row[3]=='']
	submission_train.gender = (row[4],0)[row[4]=='']
	submission_train.save()	
