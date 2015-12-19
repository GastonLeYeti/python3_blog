from django.contrib import admin
from blog.models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display   = ('titre', 'categorie', 'auteur', 'date')
    list_filter    = ('auteur','categorie', )
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'classes': ['collapse', ],
            'fields': ('titre', 'auteur', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)