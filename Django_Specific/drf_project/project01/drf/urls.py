from django.contrib import admin
from django.urls import path
from drf_app import views
# from serializers_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.index),
    # path('api/<int:pk>/', views.singleindex),
    # path('api/test/', views.test_main),
    # Serializer app
    # path('api/seri/', views.check),

]
