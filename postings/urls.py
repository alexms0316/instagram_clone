from django.urls import path
from .views import (
    PostingView, 
    PostingSearchView,
    CommentView,
    CommentSearchView,
    LikeView
)

urlpatterns = [
    path('/posting', PostingView.as_view()),
    path('/search/<int:user_id>', PostingSearchView.as_view()),
    path('/comment', CommentView.as_view()),
    path('/comment/search/<int:posting_id>', CommentSearchView.as_view()),
    path('/like', LikeView.as_view()),
    ]