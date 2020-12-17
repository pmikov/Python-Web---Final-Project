from django.contrib import admin

# Register your models here.
from recipes.models import Recipes, Comment


class CommentInline(admin.StackedInline):
    model = Comment


class CookbookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "timestamp")

    inlines = (CommentInline,)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe_id', 'user','text')

admin.site.register(Recipes, CookbookAdmin)
admin.site.register(Comment, CommentAdmin)