from django.contrib import admin
from .models import Auteur, Article

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'email')
    search_fields = ('nom', 'email')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'auteur', 'datecreation')
    list_filter = ('datecreation', 'auteur')
    search_fields = ('titre', 'description')