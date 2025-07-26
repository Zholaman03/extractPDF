from django.shortcuts import render
from django.http import HttpResponse
import PyPDF2
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
@csrf_exempt
def extract_text(request):
    if request.method == 'POST':
        print(request.FILES['pdf_file'])
        pdf_file = request.FILES['pdf_file']
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ''
        return render(request, 'index.html', {'text': text})
