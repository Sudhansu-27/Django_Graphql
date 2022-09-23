from django.contrib import admin
from api.models import Post
from api.models import Category
from api.models import ExtendUser

from django.apps import apps

admin.site.register(ExtendUser)
admin.site.register(Post)
admin.site.register(Category)

app = apps.get_app_config('graphql_auth')  

for model_name, model in app.models.items():
    admin.site.register(model)


#customize your admin panel according to you

# from .import models

# @admin.register(models.Category)

# class CatAdmin(admin.ModelAdmin):
#     list_display = [
#         'name',
#     ]