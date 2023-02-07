from django.contrib import admin
from .models import Portfolio
from .models import Update
from .models import Contact
from .models import FAQ
from .models import Banner
from .models import SocialMedia
from .models import SeoHome
from .models import SeoAbout
from .models import SeoServices
from .models import SeoPortfolio
from .models import SeoBlog
from .models import SeoContact


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ( 'id','image',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name',)


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}
    

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ( 'question',)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ( 'id','link',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ( 'category','title_first_word','title_second_word',)


@admin.register(SeoHome)
class SeoHomeAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoAbout)
class SeoAboutAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoServices)
class SeoServicesAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoPortfolio)
class SeoPortfolioAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoBlog)
class SeoBlogAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoContact)
class SeoContactAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)