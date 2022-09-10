from django.contrib import admin
from django.urls import path
from clinicalApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.PatientListView.as_view(),name='index'),
    path('create/',views.PatientCreateView.as_view()),
    path('update/<int:pk>/',views.PatientUpdateView.as_view()),
    path('delete/<int:pk>/',views.PatientDeleteView.as_view()),
    path('addData/<int:pk>/',views.addData),
    path('analyze/<int:pk>/',views.analyze),
]
