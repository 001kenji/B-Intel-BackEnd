from django.urls import path,include
from . import views


urlpatterns = [
    path('viewDB/', views.viewDB, name='veiw-database-users'),
    path('submit/',views.Commit, name='submit-for-auth'),
    path('test/',views.Test, name='submit-for-auth'),
    path('dashboard/', views.DashBoard, name='user-dashboard')
]
