from django.shortcuts import render

# Create your views here.
def visit(request):
    return render(request, 'visit/visit.html')