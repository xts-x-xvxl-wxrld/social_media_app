from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Posts)
admin.site.register(models.LikePosts)
admin.site.register(models.FollowersAccount)