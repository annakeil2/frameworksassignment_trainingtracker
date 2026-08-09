from django.db import models
from django.contrib.auth.models import AbstractUser


class Training(models.Model):
    INTERNAL = 1
    EXTERNAL = 2   
    TRAINING_TYPE = {
        INTERNAL: "Internal",
        EXTERNAL: "External"
    }
    
    ONGOING = 1
    PLANNED = 2   
    COMPLETED = 3
    FAILED = 4
    TRAINING_STATUS = {
        ONGOING: "Ongoing",
        PLANNED: "Planned",
        COMPLETED: "Completed",
        FAILED: "Failed"
    }

    id = models.AutoField(primary_key=True)
    training_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    user_id = models.IntegerField()
    training_name = models.TextField()
    training_type = models.IntegerField(
        choices=TRAINING_TYPE,
    )
    trainer_name = models.TextField()
    trainer_email = models.EmailField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    training_hours = models.IntegerField()
    organiser = models.TextField(null=True, blank=True)
    training_status = models.IntegerField(
        choices=TRAINING_STATUS
    )

    def __str__(self):
        return "Training(" + self.id + "): " + self.training_name


class Staff(AbstractUser):
    
    id = models.AutoField(primary_key=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Staff(" + self.id + ")"



class Message(models.Model):
    ACTIVE = 1
    ARCHIVED = 2   
    DELETED = 3
    MESSAGE_STATUS = {
        ACTIVE: "Active",
        ARCHIVED: "Archived",
        DELETED: "Deleted"
        }
    id = models.AutoField(primary_key=True)
    sender_user_id = models.IntegerField()
    receiver_user_id = models.IntegerField()
    body = models.CharField(max_length=65000)
    subject = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    message_status = models.IntegerField(
        choices=MESSAGE_STATUS
    )
    
    def __str__(self):
        return "Message(" + self.id + ")"
    