from django.shortcuts import render, redirect
from courseList.models import course
from courseList.forms import courseUpdate

def renderCourse(request):
    courseDetails = course.objects.all()
    return render (request, 'courseList/index.html',{'courseDetails':courseDetails})

def add(request):
    form = courseUpdate()
    if request.method == 'POST':
        form = courseUpdate(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    return render(request, 'courseList/create.html',{'form':form})

def update(request,id):
    instance = course.objects.get(id=id)
    if request.method == 'POST':
        courseUp = courseUpdate(request.POST, instance=instance)
        if courseUp.is_valid():
            courseUp.save()
            return redirect('/')
    else:
        courseUp = courseUpdate(instance=instance)
    return render(request, 'courseList/update.html', {'courseUp':courseUp})

def delete(request, id):
    courseInfo = course.objects.get(id=id)
    courseInfo.delete()        
    return redirect ('/')