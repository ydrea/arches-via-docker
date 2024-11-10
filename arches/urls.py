
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

urlpatterns = []

urlpatterns.append(path('', include('arches.urls')))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Wrap urlpatterns with i18n_patterns only if this is the main URLconf
# if settings.ROOT_URLCONF == __name__:
#     if settings.SHOW_LANGUAGE_SWITCH is True:
#         urlpatterns = i18n_patterns(*urlpatterns)

#     # Add route for i18n support
#     urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))
