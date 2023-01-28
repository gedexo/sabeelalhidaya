from multiprocessing import context
from telnetlib import GA
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from .models import Gallery
from .forms import ContactForm

def index(request):
    galleries = Gallery.objects.filter().order_by("-id")[:6]
    context = {
        "is_index" : True,
        "galleries" : galleries,
       
    }
    return render(request, 'web/index.html',context)

  
def about(request):
    context = {
        "is_about" : True
    }
    return render(request, 'web/about.html',context)


def services(request):
    context = {
        "is_services" : True,
    }
    return render(request, 'web/services.html',context)


def gallery(request):
    galleries = Gallery.objects.all()
    context = {
        "is_gallery" : True,
        "galleries" : galleries,
        
    }
    return render(request, 'web/portfolio.html',context)


def contact(request):
    forms = ContactForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_contact": True,
            "forms": forms,
        }
        return render(request, 'web/contact.html', context)
    

def ac_service(request):
    context = {
        "is_ac_service" : True,
        
    }
    return render(request,'web/pages/ac-service.html',context)


def electrical_service(request):
    context = {
        "is_electrical_service" : True,
        
    }
    return render(request,'web/pages/electrical-service.html',context)



def plumbing_service(request):
    context = {
        "is_plumbing_service" : True,
        
    }
    return render(request,'web/pages/plumbing.html',context)



def tiling_service(request):
    context = {
        "is_tiling_service" : True,
        
    }
    return render(request,'web/pages/tiling.html',context)


def painting_service(request):
    context = {
        "is_painting_service" : True,
        
    }
    return render(request,'web/pages/painting.html',context)


def masonry_service(request):
    context = {
        "is_masonry_service" : True,
        
    }
    return render(request,'web/pages/masonry.html',context)


def building_cleaning_service(request):
    context = {
        "is_building_cleaning_service" : True,
        
    }
    return render(request,'web/pages/building-cleaning.html',context)


def carpentry_service(request):
    context = {
        "is_carpentry_service" : True,
        
    }
    return render(request,'web/pages/carpentry.html',context)


def general_maintanance(request):
    context = {
        "is_general_maintanance" : True,
        
    }
    return render(request,'web/pages/general-maintanance.html',context)

def wallpaper_fixing(request):
    context = {
        "is_wallpaper_fixing" : True,
        
    }
    return render(request,'web/pages/wallpaper-fixing.html',context)


def handler404(request,exception):
    return render(request,'error/404.html', status=404)


def handler500(request):
    return render(request, 'error/500.html', status=500)