from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from project.models import User_data


def index(request):
    return render(request, 'index.html')
def oleg(request):
    return render(request, 'oleg.html')
@csrf_exempt
def auth(request):
    login=request.POST["login"]
    pas = request.POST["pass"]
    data = User_data.objects.all()
    print(data)
    return render(request, 'index.html')


# Create your views here.
