from django.db import models
from django.utils import timezone
import datetime


class Ticket(models.Model):

    class TicketStatus(models.TextChoices):
        OPEN = "Open"
        CLOSED = "Closed"
        IN_PROGRESS = "In progress"
        WAITING_FOR_SUPPORT = "Waiting for support"
        WAITING_FOR_CUSTOMER = "Waiting for customer"

    summary_text = models.CharField(max_length=200)
    details_text = models.CharField(
        max_length=500,
        default="Details here."
    )
    reported_date = models.DateTimeField("Reported")
    status = models.CharField(
        max_length=30,
        choices=TicketStatus.choices,
        default=TicketStatus.OPEN,
    )

    def __str__(self):
        return self.summary_text

    def is_new(self):
        return self.reported_date >= timezone.now() - datetime.timedelta(hours=1)

    def get_status(self):
        return self.status

    def change_status(self, status):
        self.status = status
