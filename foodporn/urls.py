"""foodporn URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

from user import views

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    validators=['flex', 'ssv'],
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^recipesave/',views.recipe.as_view()),
    # url(r'^recipeupdate/(?P<pk>[0-9]+)/$',views.updaterecipe.as_view()),
    # url(r'^user/', include('user.urls')),
    url(r'^recipe/', include('recipe.urls')),
    url(r'^comment/', include('comments.urls')),
]
