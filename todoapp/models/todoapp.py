from django.db import models
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    """Task Model"""

    class Meta(object):
        verbose_name = _(u"Task")
        verbose_name_plural = _(u"Project")




    notes = models.TextField(
        blank=True,
        verbose_name=_(u"Extra Notes"))

   
