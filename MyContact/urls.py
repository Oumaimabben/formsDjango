from django.urls import path
from .views import controleform1, controleform2, controleform3

urlpatterns = [
    path('contact/', controleform1, name='controleform1'),  # URL pour la vue controleform1
    path('contact2/', controleform2, name='controleform2'),  # URL pour la vue controleform2
    path('contact3/', controleform3, name='controleform3'),  # URL pour la vue controleform2
]
