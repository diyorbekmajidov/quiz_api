from django.contrib import admin

# Register your models here.
from .models import (
    Quiz,
    Question,
    Option,
    User,
    Result_detail,
    Result,
    Topic
)

# Register your models here.
admin.site.register(User)
admin.site.register(Result)
admin.site.register(Result_detail)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Topic)