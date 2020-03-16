from django.http import HttpResponse


# def home(request):
#     return HttpResponse("<h1>Hello World</h1>")


def home(request):
    # save data related to the request
    response = HttpResponse()
    response.write("<h1>Hello World</h1>")
    response.write("<h1>Hello World</h1>")
    response.write("<h1>Hello World</h1>")
    response.write("<h1>Hello World</h1>")
    # response.content = 'some new content'
    response.status_code = 404
    return response
