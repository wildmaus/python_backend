from django.http import HttpResponse

def say_hello(request):
    name = 'default name'
    message = 'default message'
    if request.GET.get('name'):
        name = request.GET.get('name')
    if request.GET.get('message'):
        message = request.GET.get('message')
    return HttpResponse(f'Hello {name}! {message}!')