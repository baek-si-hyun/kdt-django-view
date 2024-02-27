from django.urls import path

from post.views import PostWriteView, PostDetailView, PostUpdateView

app_name = 'post'

urlpatterns = [
    path('write/', PostWriteView.as_view(), name='write'),
    path('detail/<int:post_id>', PostDetailView.as_view(), name='detail'),
    path('update/<int:post_id>', PostUpdateView.as_view(), name='update')
]
