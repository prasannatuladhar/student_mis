from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentPageView.as_view(),name="index"),
    path('details/<int:pk>', views.StudentDetailView.as_view(),name="detail"),
    path('search/',views.search,name='search')

]
