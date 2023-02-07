from .models import SocialMedia

def main_context(request):
    social_media = SocialMedia.objects.all()
    return {
        'social_media':social_media,
        'domain':request.META['HTTP_HOST']
    }
