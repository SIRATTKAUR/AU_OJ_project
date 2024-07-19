from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from compiler.forms import CodeSubmissionForm
from compiler.views import run_code
from .models import Problems
# Create your views here.



def home(request):
    problems = Problems.objects.all()[:3]  
    return render(request, 'homepage.html', {'problems': problems})

@login_required
def problemlist(request):
    problems = Problems.objects.all()
    context = {'problems':problems}
    return render(request, 'problemlist.html', context)

@login_required
def problemdetails(request, id):
    problem = get_object_or_404(Problems, id=id)
    output_data = None

    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            code = form.cleaned_data['code']
            input_data = form.cleaned_data['input_data']
            
            output_data = run_code(language, code, input_data)
    else:
        form = CodeSubmissionForm()

    return render(request, "problemdetails.html", {"form": form, "problem": problem, "output_data": output_data})





    