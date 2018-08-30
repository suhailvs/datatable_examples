"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myapp import views
from django.urls import path, include
from datatables.views import OrderListJson
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogListAPIView)
router.register(r'authors', views.AuthorListAPIView)
router.register(r'entries', views.EntryListAPIView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('blog/data/', OrderListJson.as_view(), name='order_list_json'),
    path('blog/dt/',TemplateView.as_view(template_name="home.html"))
]
