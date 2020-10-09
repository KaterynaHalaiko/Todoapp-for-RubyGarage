from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
from django.utils.translation import ugettext as _

from .models import Student, Group, MonthJournal



class TaskAdmin(admin.ModelAdmin):
    list_display = ['notes', 'task_project']
    list_editable = ['task_project']
    list_filter = ['task_project']
    list_per_page = 10
    search_fields = ['notes']


    def view_on_site(self, obj):
        return reverse('task_edit', kwargs={'pk': obj.id})


admin.site.register(Project)
