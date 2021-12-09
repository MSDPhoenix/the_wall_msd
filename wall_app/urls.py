from django.urls import path
from . import views

urlpatterns = [
    path('wall',views.wall),
    path('post_message',views.post_message),
    path('post_comment/<int:message_id>',views.post_comment),
    path('delete_message/<int:message_id>',views.delete_message),
    path('delete_comment/<int:comment_id>',views.delete_comment), 
    # path('',views.xxxx),
    # path('',views.xxxx),
    # path('',views.xxxx),
]