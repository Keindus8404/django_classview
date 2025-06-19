"""
URL configuration for cbv_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"), # 장고에서 클래스 뷰를 사용할때 쓰는 문법
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # 예시로 추가한 상세 페이지 URL
    path('create/', views.PostCreateView.as_view(), name='post_create'),  # 예시로 추가한 생성 페이지 URL
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # 예시로 추가한 업데이트 페이지 URL
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # 예시로 추가한 삭제 페이지 URL
]
