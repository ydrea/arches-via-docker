
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

# Initial URL patterns, containing project-level URLs
urlpatterns = [
    # Add project-specific URLs here
]

# Include Arches core URLs
urlpatterns.append(path('', include('arches.urls')))

# Adds URL pattern to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Wrap urlpatterns with i18n_patterns only if this is the main URLconf
if settings.ROOT_URLCONF == __name__:
    if settings.SHOW_LANGUAGE_SWITCH is True:
        # Use i18n_patterns at the top level, wrapping all urlpatterns
        urlpatterns = i18n_patterns(*urlpatterns)

    # Add route for i18n support
    urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))
