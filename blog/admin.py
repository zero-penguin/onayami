from django.contrib import admin
from .models import Category
from .models import Tag
from .models import Question
from .models import Answer

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
