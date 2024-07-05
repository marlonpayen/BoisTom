'''
Created on 28 Jun 2024

@author: mpayen
'''
from django.template import loader
from django.http.response import HttpResponse
from website.models import Contact, Produit, Message
from website.forms import MessageForm
from django.shortcuts import render
from BoisTom.settings import MEDIA_URL, STATIC_URL
from django.template import RequestContext

def index(request):
    contact = Contact.objects.first()
    produits = Produit.objects.all()
    
    template = loader.get_template('website/index.html')
    context = {
        'contact' : contact,
        'produits' : produits,
        'MEDIA_URL' : MEDIA_URL
    }
     
    return HttpResponse(template.render(context, request))

def send_message(request):
    contact = Contact.objects.first()
    template = loader.get_template('website/messagesent.html')
    context = {
        'contact' : contact,
        'MEDIA_URL' : MEDIA_URL,
        'STATIC_URL' : STATIC_URL
    }
    
    if request.method == "POST":
        form = MessageForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return render(request, 'website/messagesent.html', {
                'form': form,
                'success': True,
                'contact' : contact,
                'MEDIA_URL' : MEDIA_URL,
                'STATIC_URL' : STATIC_URL
            })
    else:
        form = MessageForm()
    
      
    return render(request, template.render(context, request), {'form': form})
  
def my_custom_page_not_found_view(request, *args, **argv):
    response = render('website/404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def my_custom_error_view(request, *args, **argv):
    return render(request, 'website/500.html')

def my_custom_permission_denied_view(request, *args, **argv):
    return render(request, 'website/403.html')

def my_custom_bad_request_view(request, *args, **argv):
    return render(request, 'website/400.html')
  
  
    