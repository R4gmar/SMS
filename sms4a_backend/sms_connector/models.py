from django.db import models


class SMSJob(models.Model):
    recipients = models.TextField()
    template = models.TextField()
    context = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')  # 'Pending', 'Sent', 'Failed'
    objects = models.Manager()
