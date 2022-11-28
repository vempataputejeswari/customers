# import the standard Django Model
# from built-in library
from django.db import models
  
# declare a new model with a name "GeeksModel"
class customer_details(models.Model):
 
    # fields of the model
    name = models.CharField(max_length = 200)
    location = models.TextField()
    email = models.EmailField(max_length = 40)
    phone_number = models.CharField(max_length = 10)
    status = models.CharField(max_length = 20)
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name
