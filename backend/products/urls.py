from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('',views.ProductListCreateAPIView.as_view())
]
