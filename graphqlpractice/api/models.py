from pyexpat import model
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import AbstractUser

class ExtendUser(AbstractUser):
    
    email = models.EmailField(blank=False , max_length=255, verbose_name="email")
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    CATEGORY_FIELD = "Category.category"
    

class Category(models.Model):
    name = models.CharField(max_length=255)
   
    # posts = models.ManyToManyField(
    #     'Post', related_name='categories', blank=True)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=255, default=("New Post"))
    category= models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING) 
    owner = models.ForeignKey("ExtendUser", on_delete=models.PROTECT , null=True)
    # date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    

    
 
