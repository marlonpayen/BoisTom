'''
Created on 29 Oct 2023

@author: mpayen
'''
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.fields.json import JSONField
from website.util.website import constants
from django.utils import timezone


class Contact(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    pays = models.CharField(max_length=30, choices=constants.Languages_Countries.countries) # Dropdown list with all the countries defined in the constants file
    ville = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    numero_de_telephone = models.CharField(max_length=20)
    jours_d_ouverture = models.CharField(max_length=30) 
    heure_d_ouverture = models.CharField(max_length=10) 
    heure_de_fermeture = models.CharField(max_length=10)
    introduction = models.CharField(max_length=80)
    description = models.TextField() # Bigger than CharField object and text area rendered on the HTML file
    
    creation = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)
    
    # We can only have one contact, the person who is creating her own resume
    def clean(self):
        if Contact.objects.exists() and not self.pk:
            raise ValidationError('There can only be one contact')
         
         
    def save(self, *args, **kwargs):
        return super(Contact, self).save(*args, **kwargs) #saves the record
    
    # Concatenate first and last name for display
    def nom_complet(self):
        return '{} {}'.format(self.prenom, self.nom)
    
    
class Produit(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.FloatField()
    
class Lien(models.Model):
    social_media = models.TextField(choices=constants.Social_Media.social_medias)
    lien = models.TextField()
    produit = models.ForeignKey(Contact, on_delete=models.CASCADE)


class Image(models.Model):
    image = models.ImageField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    
    
class Message(models.Model):
    nom = models.CharField(max_length=50, editable = False)
    email = models.CharField(max_length=80, editable = False)
    sujet = models.CharField(max_length=100, null=True, editable = False)
    message = models.TextField(editable = False)
    date_de_creation = models.DateTimeField(default=timezone.now, editable = False)
    

    
    
    
    
    