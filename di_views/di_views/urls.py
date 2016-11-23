"""di_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from views import ContactView

class UCFormatter(object):
    def format(self, name):
        return name.upper()

class LCFormatter(object):
    def format(self, name):
        return name.lower()

# Pass the desired logic of the view here
urlpatterns = [
    # url(r'^contacts/', ContactView.as_view(formatter=UCFormatter())),
    url(r'^contacts/', ContactView.as_view(formatter=LCFormatter())),
]
