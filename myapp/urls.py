from django.urls import path
from . import views

urlpatterns = [
    # 다른 URL 패턴들
    path('text_file/', views.text_file_view, name='text_file_view'),
]