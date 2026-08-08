from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=200)
    datecreation = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='articles')
    description = models.TextField()
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.titre