'''
Created on 29 Oct 2023

@author: mpayen
'''

from django.contrib import admin
from website.models import Contact, Produit, Lien, Image, Message

class LienAdmin(admin.TabularInline):    
    model = Lien
    extra = 1
    
    
class ContactAdmin(admin.ModelAdmin):
    inlines = [LienAdmin]
    list_display = ('nom_complet', 'modification')

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if Contact.objects.exists():
            return False
        
        return True
    
admin.site.register(Contact, ContactAdmin)  
admin.site.register(Lien)  


class ImageAdmin(admin.TabularInline):    
    model = Image
    extra = 1
    
    
class ProduitAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ('nom', 'description', 'prix')

admin.site.register(Produit, ProduitAdmin) 
admin.site.register(Image) 


class MessageAdmin(admin.ModelAdmin):
    list_display = ('date_de_creation', 'nom', 'sujet', 'email', 'message')
    def has_change_permission(self, request, obj=None):
        
        return False

admin.site.register(Message, MessageAdmin) 

