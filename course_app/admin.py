from django.contrib import admin
from course_app.models import Topic, Webpage, AccessRecord,User

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(User)
