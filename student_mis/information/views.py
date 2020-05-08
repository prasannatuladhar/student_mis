from django.shortcuts import render,get_object_or_404,redirect
from .models import StudentInfo
from django.views.generic import ListView,DetailView
from django.db.models import Q


class StudentPageView(ListView):
    template_name = 'information/index.html'
    model = StudentInfo
    context_object_name = 'info'

class StudentDetailView(DetailView):
    template_name =  'information/detail.html'   
    model = StudentInfo
    context_object_name = 'student_info'

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

    
        
