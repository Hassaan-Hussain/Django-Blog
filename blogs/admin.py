from django.contrib import admin
from .models import Category, Blog, SocialLinks, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('title', 'category__category_name', 'status', 'is_featured')
    list_editable = ('is_featured',)    
    # list_display_links = ('title',)

    # function to allow for adding more data in model
    def has_add_permission(self, request):
        blog = Blog.objects.all().count()
        print(blog)
        if blog == 5:
            return False
        return True
    
class LinkAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        links = SocialLinks.objects.all().count()
        if links == 3:
            return False
        return True

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SocialLinks, LinkAdmin)
admin.site.register(Comment)
