"""
URL configuration for opportunity_analysis project.

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
from analysis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/opportunities/', views.OpportunityListCreate.as_view(), name='opportunity-list'),
    path('api/opportunities/summary/', views.OpportunitySummary.as_view(), name='opportunity-summary'),
    path('opportunities/report/', views.OpportunityReportView.as_view(), name='opportunity_report'),

    
]


