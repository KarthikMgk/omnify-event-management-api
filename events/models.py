from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.



class Events:
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.IntegerField(validators=[MinValueValidator(25)])

    def clean(self):
        super().clean()
        if self.start_time and self.end_time:
            if self.start_time > self.end_time:
                raise ValidationError("Start time must be earlier than end timeq")

    def __str__(self):
        return self.name