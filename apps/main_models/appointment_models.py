from django.db import models
from django.utils import timezone
from config.settings import AUTH_USER_MODEL
from apps.main_models.doctor_models import Doctor

class AppointmentStatus(models.TextChoices):
    RESERVED = 'reserved', 'Reserved'
    CANCELLED = 'cancelled', 'Cancelled'
    COMPLETED = 'completed', 'Completed'
    NO_SHOW = 'no_show', 'No Show' 

class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='Doctor'
    )
    patient = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments',
        limit_choices_to={"user_type": "patient"},
        verbose_name='Patient'
    )
    date = models.DateField(verbose_name='Appointment Date')
    start_time = models.TimeField(verbose_name='Start Time')
    end_time = models.TimeField(verbose_name='End Time')

    status = models.CharField(
        max_length=20,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.RESERVED
    )
    notes = models.TextField(blank=True, null=True, verbose_name='Patient Notes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', 'start_time']
        unique_together = ('doctor', 'date', 'start_time') 

    def __str__(self):
        return f"{self.date} | {self.start_time}-{self.end_time} | Dr. {self.doctor.doctor_user.last_name} & {self.patient.first_name}"
