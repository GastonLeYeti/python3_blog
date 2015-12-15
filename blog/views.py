from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>HW</h1>
              <p></p>"""
    return HttpResponse(text)