from django.shortcuts import render

# Create your views here.
def vista_pacientes(request):
    contexto ={}
    return render(request, "pacientes/vista_pacientes.html/", contexto)
