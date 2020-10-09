import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Student


@receiver(post_save, sender=task)
def log_task_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated student into log file"""
    logger = logging.getLogger(__name__)

    task = kwargs['instance']
    if kwargs['created']:
        logger.info("Task added: %s %s (ID: %d)",
            task.notes)
    else:
        logger.info("Task updated: %s %s (ID: %d)", 
            student.notes)

@receiver(post_delete, sender=task)
def log_task_deleted_event(sender, **kwargs):
    """Writes information about deleted student into log file"""
    logger = logging.getLogger(__name__)

    task = kwargs['instance']
    logger.info("Task deleted: %s %s (ID: %d)", task.notes)
