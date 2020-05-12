from django.shortcuts import render
from django.http import HttpResponse
from app.models import Course

# Create your views here.
def index(request):
    course_list = Course.objects.order_by('course_title')
    course_dict = {'course': course_list}
    return render(request, 'app/index.html', context=course_dict)

def course_detail(request, pk):
    course = Course.objects.get(pk = pk)
    cdict = {'course': [course]}
    return render(request, 'app/course.html', context=cdict)