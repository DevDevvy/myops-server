"""app_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers
from django.urls import include, path
from app_api.views import register_user, login_user
from app_api.views.checkin_view import CheckInView
from app_api.views.journal_view import JournalView
from app_api.views.mood_view import MoodView
from app_api.views.myops_user_view import MyOpsUserView
from app_api.views.tip_view import TipView
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tips', TipView, 'tip')
router.register(r'currentuser', MyOpsUserView, 'ops')
router.register(r'moods', MoodView, 'mood')
router.register(r'checkin', CheckInView, 'check')
router.register(r'journals', JournalView, 'journal')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
