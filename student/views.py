from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from student.tasks import send_sms

from .forms import StudentForm
from .models import Student


def student_list_view(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})


def edit_student(request, id: int):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse(f"No student with id {id}")
    if request.method == "GET":
        form = StudentForm(instance=student)
        context = {"form": form}
        return render(request, "edit_student.html", context)
    elif request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if not form.is_valid():
            return HttpResponse("Form is not valid")
        form.save()
        return HttpResponseRedirect(reverse('student-list'))


def delete_student(request, id: int):
    if request.method == "POST":
        student = Student.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect(reverse('student-list'))


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            send_sms.delay(form.cleaned_data['phone'])
            # send_sms.delay()
            return HttpResponseRedirect(reverse("student-list"))
    else:
        form = StudentForm()
    return render(request, "add_student.html", {"form": form})
