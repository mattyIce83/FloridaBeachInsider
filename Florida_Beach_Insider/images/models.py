from django.core.urlresolvers import reverse
from django.db import models as models
from django.core.exceptions import ValidationError

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = .5
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB. Please use http://www.imageoptimizer.net/Pages/Home.aspx to lower the file size." % str(megabyte_limit))

class Image(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    caption = models.CharField(blank=True, max_length=255)
    image = models.ImageField(upload_to="resources/images", validators=[validate_image], help_text="Max image size .5 MB.")


    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('images_image_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('images_image_update', args=(self.pk,))


