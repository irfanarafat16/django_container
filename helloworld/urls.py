from django.urls import include
from django.contrib import admin
from django.urls import path
from helloworld import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Hello, world! , contact
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('info/', views.info, name='info'),
    path('query/', views.tdata, name='tabledata'),
    path('form/', views.forminfo , name='forminput'),
    path('sapp/', include("helloapp.urls")),

]
