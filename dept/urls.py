from django.urls import path
from django.urls.resolvers import URLPattern
from dept import views

urlpatterns = [
    path('home/',views.home),
    path('student/<std_id>',views.getStudent),
    path('allstd/',views.getAllStudents),
    path('newstd/',views.addNewStd),
    path('edit/<std_id>',views.editStd),
    path('delete/<std_id>',views.deleteStd),
]