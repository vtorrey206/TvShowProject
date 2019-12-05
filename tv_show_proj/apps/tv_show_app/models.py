from django.db import models
import datetime
import relativedelta


class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:               # add keys and values to errors dictionary for each invalid field
            errors["title"] = "Title should be at least 3 characters choose a longer tv show player"
        if len(postData['network']) < 1:               # add keys and values to errors dictionary for each invalid field
            errors["network"] = "You must fill out the network if you dont know then type Unkown"
        try:
            today_date = datetime.datetime.today()
            date_entered = datetime.datetime.strptime(postData['release_date'], '%Y-%m-%d') 
            age = today_date - date_entered

            if age.years < 13:
                errors["release_date"] = "Cannot choose a future date"
        except:
            errors['release_date'] = "Invalid date."
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager() 
    # added code below old BlogManager class