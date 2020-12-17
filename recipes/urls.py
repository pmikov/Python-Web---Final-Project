from django.urls import path

from recipes.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes/', RecipesListView.as_view(), name='list recipes'),
    path('create/', CreateRecipeView.as_view(), name='create recipe'),
    path('edit/<int:pk>/', UpdateRecipeView.as_view(), name='edit recipe'),
    path('delete/<int:pk>/', DeleteRecipeView.as_view(), name='delete recipe'),
    path('details/<int:pk>/', DetailsRecipeView.as_view(), name='details recipe'),
    path('editcomment/<int:pk>/', EditCommentView.as_view(), name='edit comment'),
    path('deletecomment/<int:pk>/', DeleteCommentView.as_view(), name='delete comment'),
    path('comment/<int:pk>/', CommentRecipeView.as_view(), name='comment recipe'),
    ]