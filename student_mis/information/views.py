from django.shortcuts import render,get_object_or_404,redirect
from .models import StudentInfo
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.db.models import Q
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


class StudentPageView(ListView):
    template_name = 'information/index.html'
    model = StudentInfo
    context_object_name = 'info'

class StudentDetailView(DetailView):
    template_name =  'information/detail.html'   
    model = StudentInfo
    context_object_name = 'student_info'

class StudentInfoCreateView(CreateView):
    template_name = 'information/create.html'  
    model = StudentInfo
    fields = ['name','student_id','phone','gender','image','year_joined']
    success_url = '/'

class StudentInfoUpdateView(UpdateView):
    template_name  = 'information/update.html' 
    model = StudentInfo
    fields = ['name','student_id','phone','gender','image','year_joined']
    def form_valid(self,form):
        instance = form.save()
        return redirect('detail',instance.pk)

class StudentInfoDeleteView(DeleteView):
    template_name  = 'information/delete.html' 
    model = StudentInfo
    success_url = '/'
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request,'information/registration/login.html',{})     
    else:
        return render(request,'information/registration/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, 'Profile is Successfully logged out')
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("hello")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Profile is Successfully Created')
            return redirect('index')
    else:
        form = UserCreationForm()         
    return render(request, 'information/registration/register.html', {'form': form})

def search(request):
    if request.method == "GET":
        search_term = request.GET['search_name']
        
        if search_term != "" :
            student_info = StudentInfo.objects.filter(
                Q(name__icontains=search_term)|
                Q(student_id__icontains=search_term)|
                Q(name__icontains=search_term)|
                Q(gender__iexact=search_term) |
                Q(phone__iexact=search_term)
            )
            context = {
               'student_info':student_info,
               'search_term':search_term
                }
            return render(request,'information/search.html',context)
        else:
            return redirect('index')    
    else:
        return redirect('index')  

    
        