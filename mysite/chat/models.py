from django.db import models
# Create your models here.
class userlogin(models.Model):
    userid=models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=42)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    access=models.BooleanField()
    ctime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.userid}  |  {self.name}  |  {self.email}|  |{self.ctime}"

class Messages(models.Model):

    description = models.TextField()
    sender_name = models.ForeignKey(userlogin, on_delete=models.CASCADE, related_name='sender')
    receiver_name = models.ForeignKey(userlogin, on_delete=models.CASCADE, related_name='receiver')
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    ctime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.receiver_name.email} ---- From: {self.sender_name.email}"

    class Meta:
        ordering = ('ctime',)

