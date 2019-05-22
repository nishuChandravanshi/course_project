from django.urls import path
from course_app import views

urlpatterns=[path('index/',views.index),
# path('help/',views.help),
             path('users/',views.users),
]
