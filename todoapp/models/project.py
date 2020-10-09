from django.db import models
from django.utils.translation import ugettext_lazy as _


class Group(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = _(u"Project")
        verbose_name_plural = _(u"Project")

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Title"))


    notes = models.TextField(
        blank=True,
        verbose_name=_(u"Extra Notes"))
