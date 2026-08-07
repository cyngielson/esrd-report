"""
Django URL patterns — mapped from CICS TRANSID / COBOL entry points.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('escal056/', views.escal056_view, name='escal056'),
    path('escal062/', views.escal062_view, name='escal062'),
    path('escal070/', views.escal070_view, name='escal070'),
    path('escal071/', views.escal071_view, name='escal071'),
    path('escal080/', views.escal080_view, name='escal080'),
    path('escal091/', views.escal091_view, name='escal091'),
    path('escal100/', views.escal100_view, name='escal100'),
    path('escal117/', views.escal117_view, name='escal117'),
    path('escal122/', views.escal122_view, name='escal122'),
    path('escal130/', views.escal130_view, name='escal130'),
    path('escal140/', views.escal140_view, name='escal140'),
    path('escal151/', views.escal151_view, name='escal151'),
    path('escal160/', views.escal160_view, name='escal160'),
    path('escal170/', views.escal170_view, name='escal170'),
    path('escal171/', views.escal171_view, name='escal171'),
    path('escal180/', views.escal180_view, name='escal180'),
    path('escal191/', views.escal191_view, name='escal191'),
    path('escal200/', views.escal200_view, name='escal200'),
    path('escal202/', views.escal202_view, name='escal202'),
    path('escal212/', views.escal212_view, name='escal212'),
    path('esdrv212/', views.esdrv212_view, name='esdrv212'),
]
