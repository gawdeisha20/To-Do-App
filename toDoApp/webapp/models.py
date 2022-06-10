from django.db import models

# Create your models here.
class task(models.Model):
    tasknumber = models.IntegerField()
    taskdescription = models.CharField(max_length=70)
    #taskstatus = models.

    def __int__(self):
        return self.tasknumber