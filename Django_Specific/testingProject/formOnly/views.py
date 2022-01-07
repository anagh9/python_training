from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'GET':
        # p = request.POST['name']
        # p = request.GET['name']
        # print(p)
        print(request)
    return render(request, 'index.html')
