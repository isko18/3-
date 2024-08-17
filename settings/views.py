from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'IT PARK',
        'description': 'Курсы IT в Оше',
        
        'base': 'Главное',
        'courses': 'Курсы',
        'contact': 'Контакты'
    }
    return render(request, 'index.html', context=context)


