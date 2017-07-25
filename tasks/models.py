from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    dateCreated = models.DateField(blank=True, null=True)
    dateUpdated = models.DateField(blank=True, null=True)
    user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-dateCreated', '-dateUpdated']
