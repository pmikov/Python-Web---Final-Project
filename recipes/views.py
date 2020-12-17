import os

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
# Create your views here.

from recipes.forms import RecipesForm, CommentForm
from recipes.models import Recipes, Comment

ADMIN_USERNAME = "admin"

class IndexView(views.TemplateView):
    template_name = "landing_page.html"


class RecipesListView(views.ListView):
    model = Recipes
    template_name = "recipes/index.html"
    context_object_name = "recipes"


class CreateRecipeView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = "recipes/create.html"
    model = Recipes
    form_class = RecipesForm

    def get_success_url(self):
        url = reverse_lazy ("details recipe", kwargs = {"pk": self.object.id})
        return url

    def form_valid(self, form):
        recipe = form.save(commit = False)
        recipe.user = self.request.user.userprofile
        recipe.save()
        return super().form_valid(form)


class UpdateRecipeView(views.UpdateView):
    template_name = "recipes/edit.html"
    model = Recipes
    form_class = RecipesForm
    context_object_name = "recipe"

    def get_success_url(self):
        url = reverse_lazy ("details recipe", kwargs = {"pk": self.object.id})
        return url

    def form_valid(self, form):
        recipe = form.save(commit =False )
        recipe.save()
        return super().form_valid(form)


class DeleteRecipeView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Recipes
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("list recipes")
    context_object_name = "recipe"

    #additional check if the user can delete (apart from the if in template):
    def dispatch(self, request, *args, **kwargs):
        recipe = self.get_object()
        if request.user.username == "admin" or request.user.username == recipe.user.user.username:
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()



class DetailsRecipeView(views.DetailView):
    model = Recipes
    template_name = "recipes/details.html"
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        recipe = context[self.context_object_name]
        recipe.ingredients_list = recipe.ingredients.split(", ")
        context["own_recipe"] = self.request.user.username == recipe.user.user.username
        context["current_user"] = self.request.user.username
        context["admin"] = self.request.user.username == ADMIN_USERNAME

        return context


class CommentRecipeView(auth_mixins.LoginRequiredMixin, views.FormView):
    form_class = CommentForm

    def form_valid(self, form):
       comment = form.save(commit=False)
       comment.user = self.request.user.userprofile
       comment.recipe = Recipes.objects.get(pk=self.kwargs['pk'])
       comment.save()
       return redirect('details recipe', self.kwargs['pk'])


class EditCommentView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Comment
    template_name = "comments/edit.html"
    context_object_name = "comment"
    form_class = CommentForm

    def get_success_url(self):
        url = reverse_lazy ("details recipe", kwargs = {"pk": self.object.recipe.id})
        return url

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.save()
        return super().form_valid(form)


class DeleteCommentView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Comment
    template_name = "comments/delete.html"
    context_object_name = "comment"

    def get_success_url(self):
        url = reverse_lazy("details recipe", kwargs={"pk": self.object.recipe.id})
        return url

    #additional check if the user can delete (apart from the if in template):
    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user.username == "admin" or request.user.username == comment.user.user.username:
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()