from django.db import models
from django.core.urlresolvers import reverse


class JobPosition(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('date created')

    def get_absolute_url(self):
        return reverse("jobPosition:details", kwargs={"id": self.id})

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(default='test@gmail.com')
    phone = models.IntegerField(default=555555555)
    created = models.DateTimeField(auto_now_add=True)
    jobposition = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    is_working = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("workers:detail", kwargs={"id": self.id})

    def __str__(self):
        return self.first_name
