from django.urls import path
from posts.views import post_list, post_detail
from posts.api.api import AllWeblogs, DetailWeblog, CreateComment

app_name = 'posts'

urlpatterns = [
    # Template URLs
    path('', post_list, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    # API URLs
    path('api/', AllWeblogs.as_view(), name='api_all_weblogs'),
    path('api/<int:post_id>/', DetailWeblog.as_view(), name='api_detail_weblog'),
    path('api/<int:post_id>/comments/', CreateComment.as_view(), name='api_create_comment'),
]