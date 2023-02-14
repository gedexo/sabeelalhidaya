from multiprocessing import context
from telnetlib import GA
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from .models import Portfolio
from .models import Update
from .models import FAQ
from .models import Banner
from .models import SocialMedia
from .models import SeoHome
from .models import SeoAbout
from .models import SeoServices
from .models import SeoPortfolio
from .models import SeoBlog
from .models import SeoContact
from .forms import ContactForm

def index(request):
    portfolio = Portfolio.objects.filter().order_by("-id")[:6]
    faq = FAQ.objects.all()
    banner = Banner.objects.all().order_by("-id")
    seo_home = SeoHome.objects.all()
    context = {
        "is_index" : True,
        "portfolio" : portfolio,
        'faq':faq,
        'banner':banner,
        "seo_home":seo_home,
    }
    return render(request, 'web/index.html',context)

  
def about(request):
    seo_about = SeoAbout.objects.all()
    context = {
        "is_about" : True,
        "seo_about":seo_about,
    }
    return render(request, 'web/about.html',context)


def services(request):
    seo_services = SeoServices.objects.all()
    context = {
        "is_services" : True,
        "seo_services":seo_services,
    }
    return render(request, 'web/services.html',context)


def portfolio(request):
    portfolio = Portfolio.objects.all()
    seo_portfolio = SeoPortfolio.objects.all()
    context = {
        "is_gallery" : True,
        "portfolio" : portfolio,
        "seo_portfolio":seo_portfolio,
        
    }
    return render(request, 'web/portfolio.html',context)


def contact(request):
    seo_contact = SeoContact.objects.all()
    social_media = SocialMedia.objects.all()
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
            "social_media":social_media,
            "seo_contact":seo_contact,
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


def blog(request):
    updates=Update.objects.all()
    seo_blog = SeoBlog.objects.all()
    context = {"is_blog":True,"updates":updates,"seo_blog":seo_blog}
    return render(request,"web/blog.html",context)


def blog_details(request,slug):
    update = get_object_or_404(Update,slug=slug)
    updates=Update.objects.exclude(pk=update.pk)[:3]
    context = {"update":update,"updates":updates}
    return render(request,"web/blog-details.html",context)


def residential_cleaning(request):
    context = {
        "is_residential_cleaning":True
    }
    return render(request,'web/pages/residential-cleaning.html',context)


def sofa_cleaning(request):
    context = {
        "is_sofa_cleaning":True
    }
    return render(request,'web/pages/sofa-cleaning.html',context)


def construction_cleaning(request):
    context = {
        "is_construction_cleaning":True
    }
    return render(request,'web/pages/construction-cleaning.html',context)


def carpet_cleaning(request):
    context = {
        "is_carpet_cleaning":True
    }
    return render(request,'web/pages/carpet-cleaning.html',context)


def mattress_cleaning(request):
    context = {
        "is_mattress_cleaning":True
    }
    return render(request,'web/pages/mattress-cleaning.html',context)


def office_cleaning(request):
    context = {
        "is_office_cleaning":True
    }
    return render(request,'web/pages/office-cleaning.html',context)