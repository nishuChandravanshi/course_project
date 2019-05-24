from django.shortcuts import render
# from django.http import HttpResponse
from course_app.models import Topic,AccessRecord, Webpage, User
from course_app.form import FormName
# Create your views here.

def index(request):
    # linking models
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpage_list}
    return render(request,'course_app/index.html',context= date_dict)


            # earlier-->
    # return HttpResponse('<em>My Course_App!</em>')
    # my_dict= {'insert_me':"now im coming from course_app.html"}
    # return render(request,'course_app/index.html',context=my_dict)

# def help(request):
#
#      helpdict ={'helpkey':"welcome to helpPage!"}
#      return render(request,'course_app/help.html',context = helpdict)

def users(request):
    # userlist= User.objects.all()
    # user_dict={'user_name': userlist}

    form = FormName()

    if request.method=="POST":
        form = FormName(request.POST)

        if form.is_valid():

            form.save(commit=True)
            return index(request)

        else:
            print('invalid!') 


    return render(request, 'course_app/user.html',{'form':form})
