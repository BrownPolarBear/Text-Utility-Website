#self-made python file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def home(request):
    a='''
    <h1> Home </h1>
    <button><a href="/home">Home</a></button>
    <button><a href="/removepunc">Remove Punctuation</a></button>
    <button><a href="/capfirst">Capitalize First</a></button>
    <button><a href="/newlineremove">NewLine Remove</a></button>
    <button><a href="/spaceremove">Space Remove</a></button>
    <button><a href="/charcount">Character Count</a></button>
    '''
    return HttpResponse(a)
def analyze(request):

    djtext = request.POST.get('text', 'default')
    remove = request.POST.get('remove', 'off')
    charcount = request.POST.get('charcount','off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove= request.POST.get('extraspaceremove', 'off')
    caps = request.POST.get('caps','off')
    print(caps)
    params = {}

    punctuations = '''!()-[]{;:}'"\,<>./?@#$%^&*_~'''

    if(remove) == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params={'purpose': "Punctuation Removed/n"}
        djtext = analyzed


    if(newlineremove) == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params={'purpose': "Newlines Removed/n"}
        djtext = analyzed


    if(extraspaceremove) == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            analyzed +=char
        params={'purpose': "Extra Spaces Removed"}
        djtext = analyzed

    
    if(charcount) == "on":
        n = 0
        for char in djtext:
            if char.isalpha():
                n+=1
        djtext = djtext + ": {}".format(n)

    if(caps) == "on":
        params={'purpose': "Text Capitalized"}
        djtext = djtext.upper()    
    


    
    if remove == "off" and newlineremove =="off" and extraspaceremove == "off" and charcount == "off" and caps =="off":
        params = {'analyzed_text':"you have to perform some action on the string"}
        return render(request, 'analyze.html', params)
        
    params = {'analyzed_text': djtext}
    return render(request, 'analyze.html', params)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')
    

# def capfirst(request):
#     a = '''
#     <h1> Capitalize First </h1>
#     <button><a href="/home">Home</a></button>
#     <button><a href="/removepunc">Remove Punctuation</a></button>
#     <button><a href="/newlineremove">NewLine Remove</a></button>
#     <button><a href="/spaceremove">Space Remove</a></button>
#     <button><a href="/charcount">Character Count</a></button>
#     '''
#     return HttpResponse(a)

# def newlineremove(request):
#     a = '''
#     <h1> Capitalize First </h1>
#     <button><a href="/home">Home</a></button>
#     <button><a href="/removepunc">Remove Punctuation</a></button>
#     <button><a href="/capfirst">Capitalize First</a></button>
#     <button><a href="/spaceremove">Space Remove</a></button>
#     <button><a href="/charcount">Character Count</a></button>
#     '''
#     return HttpResponse(a)

# def spaceremove(request):
#     a = '''
#     <h1> Capitalize First </h1>
#     <button><a href="/home">Home</a></button>
#     <button><a href="/removepunc">Remove Punctuation</a></button>
#     <button><a href="/capfirst">Capitalize First</a></button>
#     <button><a href="/newlineremove">NewLine Remove</a></button>
#     <button><a href="/charcount">Character Count</a></button>
#     '''
#     return HttpResponse(a)

# def charcount(request):
#     a = '''
#     <h1> Capitalize First </h1>
#     <button><a href="/home">Home</a></button>
#     <button><a href="/removepunc">Remove Punctuation</a></button>
#     <button><a href="/capfirst">Capitalize First</a></button>
#     <button><a href="/newlineremove">NewLine Remove</a></button>
#     <button><a href="/spaceremove">Space Remove</a></button>
#     '''
#     return HttpResponse(a)
