from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


class Task(models.Model):
    STATUS = (
        ("new", "created"),
        ("planned", "planned"),
        ("in_work", "in work"),
        ("done", "done")
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # TODO try IntegerChoices then
    status = models.CharField(max_length=10, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_end = models.DateField(null=True, blank=True)

    def __srt__(self):
        return f"{self.title}: {self.status}"


class ChangeHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    changed_to = models.JSONField()

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return f"{self.task}: {self.changed_to}"
