from django.db import models

class Result(models.Model):
  date = models.DateTimeField
  key = models.CharField(max_length=240)
  value = models.IntegerField()

  def __str__(self):
    return self.key, self.date
 