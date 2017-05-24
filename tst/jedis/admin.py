# Register your models here.
from django.contrib import admin
from jedis.models import Planet, Jedi, Questions
admin.site.register(Planet)
admin.site.register(Jedi)
admin.site.register(Questions)