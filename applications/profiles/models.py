from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    username = models.CharField(max_length=150, default='')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)
    
    def generate_default_username(self):
        return f"{self.user.id}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = "User000" + self.generate_default_username()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.user.email)