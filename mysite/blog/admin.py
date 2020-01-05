from django.contrib import admin
from .models import Post

# Register your models here.

#Now, we will take a look at how to customize the admin site.
# Edit the admin.py file of your blog application and change it, as follows


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = ('publish')
    ordering = ('status', 'publish')


#     You can see that the fields displayed on the post ---
#     list page are the
# ones you specified in the ----list_display---- attribute. The list page now
# includes a right sidebar that allows you to filter the results by the
# fields included in the list_filter attribute.
#
# A Search bar has appeared
# on the page. This is because we have defined a list of searchable
# fields using the --search_fields attribute.
#
# Just below the Search bar,
# there are navigation links to navigate through a date hierarchy: this
# has been defined by the ----date_hierarchy attribute. You can also see that
# the posts are ordered by Status and Publish columns by default.
#
# We
# have specified the default order using the ordering attribute.
# Now, click on the Add Post link. You will also note some changes
# here. As you type the title of a new post,the slug field is filled in
# automatically. We have told Django to -----prepopulate the slug field
# with the input of the title field using the ----prepopulated_fields attribute.



# Also, now, the ---author field is displayed with a lookup widget that can
# scale much better than a drop-down select input when you have
# thousands of users, as shown in the following screenshot:
# With a few lines of code, we have customized the way our model is
# displayed on the admin site. There are plenty of ways to customize
# and extend the Django administration site. You will learn more
# about this later in this book.

