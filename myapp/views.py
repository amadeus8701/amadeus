# myapp/views.py
from django.shortcuts import render
from myapp.models import TextFileContent

def index(request):
    text_file_content = TextFileContent.objects.first()
    if text_file_content:
        content_lines = text_file_content.content.splitlines()[-15:]
    else:
        content_lines = []

    return render(request, 'myapp/index.html', {'content_lines': content_lines})