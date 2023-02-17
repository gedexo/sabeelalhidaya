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


@admin.register(SeoACServiceAndRepairs)
class SeoACServiceAndRepairsAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoElectricals)
class SeoElectricalsAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoPlumbing)
class SeoPlumbingAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoTiling)
class SeoTilingAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoPainting)
class SeoPaintingAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoCarpentry)
class SeoCarpentryAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoMasonry)
class SeoMasonryAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoWallpaperFixing)
class SeoWallpaperFixingAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoGeneralMaintenance)
class SeoGeneralMaintenanceAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoBuildingCleaning)
class SeoBuildingCleaningAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoResidentialCleaning)
class SeoResidentialCleaningAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoSofaCleaning)
class SeoSofaCleaningAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoConstructionCleaning)
class SeoConstructionCleaningAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoCarpetCleaning)
class SeoCarpetCleaningAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoMattressCleaning)
class SeoMattressCleaningAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)


@admin.register(SeoOfficeCleaning)
class SeoOfficeCleaningAdmin(admin.ModelAdmin):
    list_display = ( 'title','meta_keywords',)