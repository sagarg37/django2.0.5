from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')



class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),

    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
                    # This is a field intended to be used in URLs. A slug is a
                    # short label that contains only letters, numbers, underscores,
                    # or hyphens. We will use the slug field to build beautiful, SEOfriendly
                    # URLs for our blog posts. We have added the
                    # unique_for_date parameter to this field so that we can build
                    # URLs for posts using their publish date and slug. Django will
                    # prevent multiple posts from having the same slug for a
                    # given date.
    author = models.ForeignKey(User, on_delete= models.CASCADE,
                                    related_name='blog_posts')
                     # We specifythe name of the reverse relationship, from User to Post,
                     #  withthe related_name attribute.
                     #  This will allow us to access related objects easily

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
                     # This datetime indicates when the post was published.
                     # We use Django's timezone now method as the default value.
                     # This returns the current datetime in a timezone-aware
                     # format. You can think of it as a timezone-aware version of
                     # the standard Python datetime.now method.
    created = models.DateTimeField(auto_now_add=True)
                     # auto_now_add ---This datetime indicates when the post was created.
                     # Since we are using auto_now_add here, the date will be saved
                     # automatically when creating an object.
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.




    class Meta:
            ordering = ('-publish',)

                    # The Meta class inside the model contains metadata. We tell Django to
                    # sort results in the publish field in descending order by default when
                    # we query the database. We specify descending order using the
                    # negative prefix. By doing so, posts published recently will appear
                    # first.



    def __str__(self):
        return self.title

                    # The __str__() method is the default human-readable representation
                    # of the object. Django will use it in many places, such as the
                    # administration site.

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
# If you edit your models.py file in order to add, remove, or change fields
# of existing models, or if you add new models, you will have to
# create a new migration using the makemigrations command. The
# migration will allow Django to keep track of model changes. Then,
# you will have to apply it with the migrate command to keep the
# database in sync with your models.



