from django.db import models

class Result(models.Model):
  date = models.DateTimeField(auto_now=True, null=True, editable=True)
  key = models.CharField(max_length=240)
  value = models.IntegerField()

  def __str__(self):
    return (str(self.key) + "   " + str(self.date))
 