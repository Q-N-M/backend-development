from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Community)
admin.site.register(Transport)
admin.site.register(Activity)
admin.site.register(Emoji)
admin.site.register(UserEmoji)
