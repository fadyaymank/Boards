from django.contrib import admin
from django.urls import path
from boards import views

urlpatterns = [

    path('', views.BoardListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('boards/<board_id>/', views.boards_topics, name='board_topics'),
    path('boards/<board_id>/new/', views.new_topic, name='new_topic'),
    path('boards/<board_id>/topics/<topic_id>', views.topic_posts, name='topic_posts'),
    path('boards/<board_id>/topics/<topic_id>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]
