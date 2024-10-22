from Library.models import Mentor,Course
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def newmentor(request):
    if request.method == 'POST':
        men_id = request.POST.get('menid')
        men_name = request.POST.get('menname')
        men_room_no = request.POST.get('menroomno')

        if men_id and men_name and men_room_no:
            data = Mentor(menid=men_id, menname=men_name,menroomno=men_room_no)
            data.save()
            message = 'Data Saved'
        else:
            message = ''
        
        mentors = Mentor.objects.all()
        
        context = {
            'mentors': mentors,
            
        }
    else:
        mentors = Mentor.objects.all()
        context = {
            'mentors': mentors,
            'message': ''
        }

    return render(request, 'menroon.html', context)

def course(request):
    if request.method == 'POST':
        c_code=request.POST.get('code')
        c_desc=request.POST.get('description')

        if c_code and c_desc:
            data= Course(code=c_code,description=c_desc)
            data.save()
            message='Data Saved'
        else:
            message=""

        courses = Course.objects.all()

        context = {
            'code':c_code,
            'desc':c_desc,
            'course':courses
        }
    else:
        courses = Course.objects.all()
        context={
            'course':courses,
            'message':""
        }
    
    return render(request, 'course.html', context)
        

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data
    }
    return render (request,'update_course.html', dict)

def save_update_course(request,code):
    c_desc=request.POST['description']
    data=Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')

        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None

        context = {
            'data': data
        }

        return render(request, "search_course.html", context)

    return render(request, "search_course.html")