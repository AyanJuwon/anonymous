from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    
    # message
    # autoslug with username nahh
    # create view that shows dashboard to only logged in users,
    
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # message_id = models.IntegerField(auto_created=),
    message = models.TextField(max_length=256,)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.message}-{self.user}"