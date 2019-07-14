# This file created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    text = request.POST.get('text', 'default')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        text = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in text:
            analyzed += char.upper()
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed}
        text = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed Newline From Your Text', 'analyzed_text': analyzed}
        text = analyzed

    if extraspaceremover == "on":
        while "  " in text:
            text = text.replace("  "," ")
        params = {'purpose': 'Removed NewLines', 'analyzed_text': text}

    if charcount == "on":
        count = 0
        for char in text:
            count += 1
        analyzed = f"Character count of {text} is {count}"
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("PLEASE SELECT ANY OPERATION")

    return render(request, 'analyze.html', params)
