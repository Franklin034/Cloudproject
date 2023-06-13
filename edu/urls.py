from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    VideoListView,
    VideoDetailView,
    UserPostListView,
    ChoiceListView,
    MigrationListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='edu-home'),
    path('user/<str:username>',  UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('learn/', VideoListView.as_view(), name='edu-learn'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('assessment/', views.assessment, name='edu-assessment'),
    path('cloud_choice/', ChoiceListView.as_view(), name='edu-cloud_choice'),
    path('migration/', MigrationListView.as_view(), name='edu-migration'),
    path('about/', views.about, name='edu-about'),
]
 


