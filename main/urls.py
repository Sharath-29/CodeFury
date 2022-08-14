from django.urls import path
from .views import home, follow, unfollow, post, search, add_comment, add_subcomment, chat_page, email,funding_view, charge


urlpatterns = [
    path('', home, name = 'home'),
    path('search', search, name='search'),
    path('follow', follow),
    path('unfollow', unfollow),
    path('post', post),
    path('add_comment', add_comment),
    path('add_subcomment', add_subcomment),
    path('chat_page', chat_page),
    path('email', email),
    path('emailrejected', email),
    path('funding', funding_view.as_view(), name='funding'),
    path('charge',charge, name='charge'),
]
