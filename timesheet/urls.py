
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Django authentication urls
    path('accounts/', include('django.contrib.auth.urls')), # Are you using Buit-in views as it is? I see you have password-reset used in login template. 

    # Users potal
    re_path('hospital_aministration/', include('user.urls')),

    # Public access (Readers)
    re_path('', include('reader.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
