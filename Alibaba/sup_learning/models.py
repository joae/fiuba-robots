from django.db import models

class SubmissionTest(models.Model):
	user_id = models.IntegerField()
	merchant_id = models.IntegerField()
	prob = models.IntegerField()

	class Meta:
		managed = True
		db_table = 'submission_test'

class SubmissionTrain(models.Model):
	user_id = models.IntegerField()
	merchant_id = models.IntegerField()
	prob = models.IntegerField()

	class Meta:
		managed = True
		db_table = 'submission_train'		