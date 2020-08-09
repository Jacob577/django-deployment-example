from django.urls import path,include
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailedView.as_view(),name='detail'),
    # path('<int:pk>/',views.StudentlDetailedView.as_view(),name='detailstudent'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('addstudent/',views.StudentCreateView.as_view(),name='addstudent'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),
    # path('updat/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
]
