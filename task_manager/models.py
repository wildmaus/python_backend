from django.db import models


class Task(models.Model):
    STATUS = (
        ("new", "created"),
        ("planned", "planned"),
        ("in_work", "in work"),
        ("done", "done")
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # TODO try IntegerChoices then
    status = models.CharField(max_length=10, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_end = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('-status', 'date_created')

    def __srt__(self):
        return f"{self.title}: {self.status}"


class StatusChangeHistory(models.Model):
    # TODO refactor changed_to
    STATUS = (
        ("new", "created"),
        ("planned", "planned"),
        ("in_work", "in work"),
        ("done", "done")
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    changed_to = models.CharField(max_length=10, choices=STATUS)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return f"{self.task} -> {self.changed_to}"
