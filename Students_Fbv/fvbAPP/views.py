from django.shortcuts import render, redirect
from fvbAPP.models import studentInfo
from fvbAPP.forms import studentList
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def index(request):
    students = studentInfo.objects.all()
    return render (request, 'fvbAPP/index.html',{'students':students})

@login_required
def create(request):
    form = studentList()
    if request.method == 'POST':
        form = studentList(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'fvbAPP/create.html',{'form':form})

@login_required
@permission_required('fvbApp.delete_studentInfo')
def delete(request,id):
    student = studentInfo.objects.get(id=id)
    student.delete()
    return redirect('/')

@login_required
def update(request, id):
    instance = studentInfo.objects.get(id=id)
    if request.method == 'POST':
        form = studentList(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = studentList(instance=instance)

    return render(request, 'fvbAPP/update.html', {'form': form})


def logout(request):
    return render(request, 'fvbAPP/logout.html')