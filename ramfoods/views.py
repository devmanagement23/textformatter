from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Duniya")

def about(request):
    return HttpResponse("<h1>This is about page.Press back to <a href='/'>return</a></h1>")

# def home(request):
#     return render(request,'home.html')

def home2(request):
    return render(request,'home2.html')

def home3(request):
    params = {'name':'ramji','place':'bharat'}
    return render(request,'home3.html',params)

# def removepunc(request):    
#     return HttpResponse("Remove punctuations")

# def removepunc(request):
#     print(request.GET.get('textdata','default'))    
#     return HttpResponse("Remove punctuations")

def removepunc(request):
    mytext = request.GET.get('textdata','default')
    print(mytext)
    return HttpResponse("Remove punctuations")

def capfirst(request):
    return HttpResponse("captialize First Alphabet")


def editor(request):
    return render(request,'editor.html')

def edit(request):
    mytext = request.GET.get('textdata','default')
    is_removepunctuation = request.GET.get('removepunctuation','off')
    is_all_Uppercase = request.GET.get('all_uppercase','off')

    print(mytext)
    print(is_removepunctuation)
    
    if is_removepunctuation == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        formatted_data = ""

        for char in mytext:
            if char not in punctuations:
                formatted_data = formatted_data + char

        params = {'purpose':'Removed Puncatuations','data':formatted_data}
        return render(request,'formatted.html',params)

    elif(is_all_Uppercase == "on"):
        formatted_data = ""

        for char in mytext:
            formatted_data = formatted_data + char.upper()
        
        params = {'purpose':'All Uppercase','data':formatted_data}
        return render(request,'formatted.html',params)

    else:
        return HttpResponse("ERROR -- <a href='/editor'>Return</a>")
    