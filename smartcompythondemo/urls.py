"""
URL configuration for smartcompythondemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from debug_toolbar.toolbar import debug_toolbar_urls
from customerrequest.better_view import CustomerRequestRetrieveUpdateDestroyAPIView
from customerrequest.custom_api_views import CustomerRequestListCreateAPIView
from customerrequest.views import FacilityListCreateAPIView, FacilityHasAppLinkListCreateAPIView
from customerrequest.views import FacilityListRetrieveUpdateDestroyAPIView
from hello.templates.hello import say_hello
from hello.templates.hello import say_hello_with_name
from hello.views import index
from smartcompythondemo.views import ProductListCreateAPIView

# from customerrequest.views import customerrequests, customer_request
# from customerrequest.better_view import CustomerRequestListCreateAPIView, CustomerRequestRetrieveUpdateDestroyAPIView


urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('products/', ProductListCreateAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('hello/', index),
    path('', say_hello),
    path('say_hello/<name>', say_hello_with_name),
    # path('customerrequests/', customerrequests),
    # path('customerrequests/<id>', customer_request)

    # path('customerrequests/', CustomerRequestListCreateAPIView.as_view()),
    path('customerrequests/<id>', CustomerRequestRetrieveUpdateDestroyAPIView.as_view()),


    path('customerrequests/', CustomerRequestListCreateAPIView.as_view()),


    path('facility/<int:pk>', FacilityListRetrieveUpdateDestroyAPIView.as_view()),
    path('facility', FacilityListCreateAPIView.as_view()),
    path('facility/<int:facility_id>/facilitylinks', FacilityHasAppLinkListCreateAPIView.as_view()),
]+ debug_toolbar_urls()
