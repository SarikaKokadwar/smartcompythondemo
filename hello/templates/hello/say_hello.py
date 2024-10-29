from django.http import HttpResponse, HttpRequest

def say_hello(request):
    print("This is within view")
    return HttpResponse("Its my first project")


def say_hello_with_name(request: HttpRequest, name):
    print(request.headers)
    return HttpResponse("Its my first project, %s" % name)