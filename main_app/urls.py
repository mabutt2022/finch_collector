from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finch/', views.finch_index, name='index'),
    path('finch/<int:finch_id>/', views.finch_detail, name='detail'),
    path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finch/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    path('finch/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finch/<int:finch_id>/assoc_toy/<int:feature_id>/', views.assoc_feature, name='assoc_feature'),
    
    # Features
    path('features/', views.FeatureList.as_view(), name='feature_index'),
    path('features/<int:pk>/', views.FeatureDetail.as_view(), name='feature_detail'),
    path('features/create/', views.FeatureCreate.as_view(), name='feature_create'),
    path('features/<int:pk>/update/', views.FeatureUpdate.as_view(), name='feature_update'),
    path('features/<int:pk>/delete/', views.FeatureDelete.as_view(), name='feature_delete'),
    ]
