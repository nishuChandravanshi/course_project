from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name= models.CharField(max_length=260,unique=True)


    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  #=> topic must be a Topic instance(ie it can only be assigned the values of Topic attributes and not any other random values)
    name = models.CharField(max_length=260,unique=True)
    url = models.URLField(unique=True)


    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)   #self.date int type--can be represented as string using str func


class User(models.Model):
    first_name= models.CharField(max_length=150)
    last_name= models.CharField(max_length=150)
    email  =models.EmailField(max_length=150,unique=True)

    def __str__(self):
        return self.first_name
