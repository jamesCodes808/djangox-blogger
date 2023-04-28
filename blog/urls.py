from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='blog_post_list_view'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog_post_detail_view'),
    path('create-post/', PostCreateView.as_view(), name='blog_post_create_view'),
    path('<int:pk>/update-post/', PostUpdateView.as_view(), name='blog_post_update_view'),
    path('<int:pk>/delete-post/', PostDeleteView.as_view(), name='blog_post_delete_view'),
]