from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .forms import AddStudentForm
# Create your views here.

class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'crudapp/home.html', {'studata': stu_data})
    
class Add_Student(View):
    def get(save, request):
        fm= AddStudentForm()
        return render(request, 'crudapp/add-student.html', {'form': fm})
    
    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'crudapp/add-student.html', {'form': fm})
        
class Delete_Student(View):
    def post(self, request):
        id = request.POST.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')
    
class EditStudent(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'crudapp/edit-student.html', {'form':fm})
    def post(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')