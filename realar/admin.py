from django.contrib import admin
from .models import List
from .models import Post, Category



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
    search_fields = ['name'] 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'author', 'categories')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['author', 'categories']
    filter_horizontal = ['categories']




class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_data')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

    # Explicitly include the fields in the form view
    fields = (
        
        'description','title', 'price','address', 'city', 'state', 
        'zipcode',  'bedrooms', 'bathrooms', 'garage',
        'sqft', 'lot_size', 'photo_main', 'photo_1', 'photo_2',
        'photo_3', 'photo_4', 'photo_5', 'photo_6', 'is_published',
        'youtube_video_url', 'google_profile_url', 'list_data'
        
    )


admin.site.register(List, ListAdmin)


