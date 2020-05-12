from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentPageView.as_view(),name="index"),
    path('details/<int:pk>', views.StudentDetailView.as_view(),name="detail"),
    path('search/',views.search,name='search'),
    path('create/',views.StudentInfoCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.StudentInfoUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.StudentInfoDeleteView.as_view(),name='delete'),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),



]
