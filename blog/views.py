from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
#from . import templates

def home(request):
    return render(request, 'blog/home.html')
  
  
def view_article(request, id_article):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """

    text = "Vous avez demandé l'article #{0} !".format(id_article)
    return HttpResponse(text)
  
  
  
def list_articles(request, year, month):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)
  
  


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())