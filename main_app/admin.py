from django.contrib import admin
# import your models here
from .models import Finch, Feeding, Features, Photo

# Register your models here
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Features)
admin.site.register(Photo)
