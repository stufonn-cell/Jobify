"""
URL configuration for Jobify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landingPage.views import lpView 
from editPage.views import step1, step2, step3
from history.views import history_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lpView),
    path('historial/', history_view),
    path('nueva_vacante/paso1/', step1),
    path('nueva_vacante/paso1/paso2/', step2),
    path('nueva_vacante/paso1/paso2/paso3/', step3)
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)