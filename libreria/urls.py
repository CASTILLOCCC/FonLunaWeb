from django.urls import path
from.import views
from django.shortcuts import render
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include




urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('Asociados', views.Asociados, name='Asociados'),
    path('Asociados/create', views.create, name='create'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('Asociados/<int:id>', views.edit, name='edit'),
    path('Aportes/create_aporte', views.create_aportes, name='create_aporte'),
    path('Aportes', views.Aportes, name='Aportes'),
    path('Aportes/<int:id>', views.edit_aportes, name='edit_aportes'),
    path('buscar_asociados/', views.search_asociados, name='buscar_asociados'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



