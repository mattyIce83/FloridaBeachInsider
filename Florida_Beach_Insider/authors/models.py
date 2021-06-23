from django.core.urlresolvers import reverse
from django.db import models as models
from django.core.exceptions import ValidationError

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = .5
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB. Please use http://www.imageoptimizer.net/Pages/Home.aspx to lower the file size." % str(megabyte_limit))

class Author(models.Model):

    # Fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug_name = models.CharField(max_length=70,unique=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    bio = models.CharField(max_length=255)
    photo = models.ImageField(blank=True, upload_to="images/authors", validators=[validate_image], help_text="Max image size .5 MB.")
    email = models.EmailField(blank=True)
    facebook = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True,max_length=30)
    instagram = models.CharField(blank=True,max_length=30)


    class Meta:
        ordering = ('last_name','first_name')

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('authors_author_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('authors_author_update', args=(self.pk,))


