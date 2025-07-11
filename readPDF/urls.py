from django.urls import path
from readPDF.views import index, extract_text
urlpatterns = [
    path('', index, name='index'),
    path('extract', extract_text, name='extract_text'),
    # Add more URL patterns as needed
]