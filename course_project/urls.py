"""course_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from course_app import views
# or instead of importing each function from views we can create a urls.py file in the app and then include it her
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # ** path('indexfun',views.index, name='index'),
    path('admin/', admin.site.urls),
    # ** first line here can be done as below as well
    path('course_app/',include('course_app.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
#  note--> the last part after the list is important while using static files and dont forget to import settings
