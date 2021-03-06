from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('clustering/<int:id>/', views.clustering, name='clustering'),
    path('dd/', views.dd, name='dd'),
    path('download/<str:path>', views.download, name='download'),
    path('output_delete/<str:path>', views.output_delete, name='output_delete'),
]
