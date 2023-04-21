from django.urls import path
from blog.views import AuthView, Postlist

urlpatterns = [
    path('api-auth/', AuthView.as_view(), name='auth_view'),
    path('posts/', Postlist.as_view(), name='post_list'),
]
