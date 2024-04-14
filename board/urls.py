from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'board'

urlpatterns = [
    path('create_board/', views.board, name='create_board'),
    path('board_detail/<int:board_id>/', views.read, name='board_detail'),
    path('board_edit/<int:pk>', views.boardEdit, name='edit'),
    path('delete/<int:pk>', views.boardDelete, name='delete'),
    path('comment_create/<int:pk>/', views.comment_create, name='comment_create'),
    path('comments/<int:board_pk>/delete/<int:comment_pk>/', views.comment_delete, name='comments_delete'),   
    path('board_list/', views.boardList, name = 'board_list'),
]