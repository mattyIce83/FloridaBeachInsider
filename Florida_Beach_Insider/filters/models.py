from django.core.urlresolvers import reverse
from django.db import models as models

class Filter(models.Model):

    # Fields
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('filters_filter_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('filters_filter_update', args=(self.pk,))


