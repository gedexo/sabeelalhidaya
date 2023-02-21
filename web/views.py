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
from .models import SeoACServiceAndRepairs
from .models import SeoElectricals
from .models import SeoPlumbing
from .models import SeoTiling
from .models import SeoPainting
from .models import SeoCarpentry
from .models import SeoMasonry
from .models import SeoWallpaperFixing
from .models import SeoGeneralMaintenance
from .models import SeoBuildingCleaning
from .models import SeoResidentialCleaning
from .models import SeoSofaCleaning
from .models import SeoConstructionCleaning
from .models import SeoCarpetCleaning
from .models import SeoMattressCleaning
from .models import SeoOfficeCleaning
from .forms import ContactForm



def index(request):
    portfolio = Portfolio.objects.filter().order_by("-id")[:6]
    faq = FAQ.objects.all()
    banner = Banner.objects.all().order_by("-id")
    seo_home = SeoHome.objects.all().last()
    context = {
        "is_index" : True,
        "portfolio" : portfolio,
        'faq':faq,
        'banner':banner,
        "seo_home":seo_home,
    }
    return render(request, 'web/index.html',context)

  
def about(request):
    seo_about = SeoAbout.objects.all().last()
    context = {
        "is_about" : True,
        "seo_about":seo_about,
    }
    return render(request, 'web/about.html',context)


def services(request):
    seo_services = SeoServices.objects.all().last()
    context = {
        "is_services" : True,
        "seo_services":seo_services,
    }
    return render(request, 'web/services.html',context)


def portfolio(request):
    portfolio = Portfolio.objects.all()
    seo_portfolio = SeoPortfolio.objects.all().last()
    context = {
        "is_gallery" : True,
        "portfolio" : portfolio,
        "seo_portfolio":seo_portfolio,
        
    }
    return render(request, 'web/portfolio.html',context)


def contact(request):
    seo_contact = SeoContact.objects.all().last()
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
    seo_ac_service = SeoACServiceAndRepairs.objects.all().last()
    context = {
        "is_ac_service" : True,
        "seo_ac_service":seo_ac_service,
    }
    return render(request,'web/pages/ac-service.html',context)


def electrical_service(request):
    seo_electrical=SeoElectricals.objects.all().last()
    context = {
        "is_electrical_service" : True,
        "seo_electrical":seo_electrical,
    }
    return render(request,'web/pages/electrical-service.html',context)



def plumbing_service(request):
    seo_plumbing = SeoPlumbing.objects.all().last()
    context = {
        "is_plumbing_service" : True,
        "seo_plumbing":seo_plumbing,
    }
    return render(request,'web/pages/plumbing.html',context)



def tiling_service(request):
    seo_tiling = SeoTiling.objects.all().last()
    context = {
        "is_tiling_service" : True,
        "seo_tiling":seo_tiling,
    }
    return render(request,'web/pages/tiling.html',context)


def painting_service(request):
    seo_painting = SeoPainting.objects.all().last()
    context = {
        "is_painting_service" : True,
        "seo_painting":seo_painting,
    }
    return render(request,'web/pages/painting.html',context)


def masonry_service(request):
    seo_mansory = SeoMasonry.objects.all().last()
    context = {
        "is_masonry_service" : True,
        "seo_mansory":seo_mansory,
    }
    return render(request,'web/pages/masonry.html',context)


def building_cleaning_service(request):
    seo_building_cleaning = SeoBuildingCleaning.objects.all().last()
    context = {
        "is_building_cleaning_service" : True,
        "seo_building_cleaning":seo_building_cleaning,
    }
    return render(request,'web/pages/building-cleaning.html',context)


def carpentry_service(request):
    seo_carpentry = SeoCarpentry.objects.all().last()
    context = {
        "is_carpentry_service" : True,
        "seo_carpentry":seo_carpentry,
    }
    return render(request,'web/pages/carpentry.html',context)


def general_maintanance(request):
    seo_general_maintenance = SeoGeneralMaintenance.objects.all().last()
    context = {
        "is_general_maintanance" : True,
        "seo_general_maintenance":seo_general_maintenance,
    }
    return render(request,'web/pages/general-maintanance.html',context)


def wallpaper_fixing(request):
    seo_wallpepper_fixing = SeoWallpaperFixing.objects.all().last()
    context = {
        "is_wallpaper_fixing" : True,
        "seo_wallpepper_fixing":seo_wallpepper_fixing,
    }
    return render(request,'web/pages/wallpaper-fixing.html',context)


def handler404(request,exception):
    return render(request,'error/404.html', status=404)


def handler500(request):
    return render(request, 'error/500.html', status=500)


def blog(request):
    updates=Update.objects.all()
    seo_blog = SeoBlog.objects.all().last()
    context = {"is_blog":True,"updates":updates,"seo_blog":seo_blog}
    return render(request,"web/blog.html",context)


def blog_details(request,slug):
    update = get_object_or_404(Update,slug=slug)
    updates=Update.objects.exclude(pk=update.pk)[:3]
    context = {"update":update,"updates":updates}
    return render(request,"web/blog-details.html",context)


def residential_cleaning(request):
    seo_residential_cleaning = SeoResidentialCleaning.objects.all().last()
    context = {
        "is_residential_cleaning":True,
        "seo_residential_cleaning":seo_residential_cleaning,
    }
    return render(request,'web/pages/residential-cleaning.html',context)


def sofa_cleaning(request):
    seo_sofa_cleaning = SeoSofaCleaning.objects.all().last()
    context = {
        "is_sofa_cleaning":True,
        "seo_sofa_cleaning":seo_sofa_cleaning,
    }
    return render(request,'web/pages/sofa-cleaning.html',context)


def construction_cleaning(request):
    seo_construction_cleaning = SeoConstructionCleaning.objects.all().last()
    context = {
        "is_construction_cleaning":True,
        "seo_construction_cleaning":seo_construction_cleaning,
    }
    return render(request,'web/pages/construction-cleaning.html',context)


def carpet_cleaning(request):
    seo_carpet_cleaning = SeoCarpetCleaning.objects.all().last()
    context = {
        "is_carpet_cleaning":True,
        "seo_carpet_cleaning":seo_carpet_cleaning,
    }
    return render(request,'web/pages/carpet-cleaning.html',context)


def mattress_cleaning(request):
    seo_mattress_cleaning = SeoMattressCleaning.objects.all().last()
    context = {
        "is_mattress_cleaning":True,
        "seo_mattress_cleaning":seo_mattress_cleaning,
    }
    return render(request,'web/pages/mattress-cleaning.html',context)


def office_cleaning(request):
    seo_office_cleaning = SeoOfficeCleaning.objects.all().last()
    context = {
        "is_office_cleaning":True,
        "seo_office_cleaning":seo_office_cleaning,
    }
    return render(request,'web/pages/office-cleaning.html',context)