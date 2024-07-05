"""
URL configuration for diabetes_prediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from diabetes_predictor import views as svc
from diabetes_LR import views as lr
from diabetes_GB import views as gb
from diabetes_DT import views as dt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('svc',svc.home),
    path('prediction_svc',svc.index),
    path('home_svc',svc.home),
    path('predict_diabetes_svc',svc.predict_diabetes),
    path('history_svc',svc.history),
    path('collect_svc',svc.update),

    path('lr',lr.home),
    path('prediction_lr',lr.index),
    path('home_lr',lr.home),
    path('predict_diabetes_lr',lr.predict_diabetes),
    path('history_lr',lr.history),
    path('collect_lr',lr.update),

    path('gb',gb.home),
    path('prediction_gb',gb.index),
    path('home_gb',gb.home),
    path('predict_diabetes_gb',gb.predict_diabetes),
    path('history_gb',gb.history),
    path('collect_gb',gb.update),

    path('dt',dt.home),
    path('prediction_dt',dt.index),
    path('home_dt',dt.home),
    path('predict_diabetes_dt',dt.predict_diabetes),
    path('history_dt',dt.history),
    path('collect_dt',dt.update),
]
