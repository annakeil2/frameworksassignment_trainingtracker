from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Training(models.Model):
    """ A record of an Employee's training """
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
        choices=TRAINING_TYPE.items()
    )
    trainer_name = models.TextField()
    trainer_email = models.EmailField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    training_hours = models.IntegerField()
    organiser = models.TextField(null=True, blank=True)
    training_status = models.IntegerField(
        choices=TRAINING_STATUS.items()
    )


    def __str__(self):
        """Return a readable representation of the training."""
        return f"Training({self.id}): {self.training_name}"


class Employee(AbstractUser):
    """An employee who can use the training system."""
    id = models.AutoField(primary_key=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Employee({self.id}, {self.username})"


class Message(models.Model):
    """A message sent between employees."""
    ACTIVE = 1
    ARCHIVED = 2   
    DELETED = 3
    MESSAGE_STATUS = {
        ACTIVE: "Active",
        ARCHIVED: "Archived",
        DELETED: "Deleted"
    }
    id = models.AutoField(primary_key=True)
    sender_user_id = models.IntegerField(null=True)
    receiver_user_id = models.IntegerField()
    body = models.CharField(max_length=65000)
    subject = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    message_status = models.IntegerField(
        choices=MESSAGE_STATUS.items()
    )
    
    
    def __str__(self):
        """Return a readable representation of the message."""
        return f"Message({self.id})"
    
    
class EmployeeManager(BaseUserManager):
    """Methods for creating employee user accounts."""
    
    def create_user(self, email, password=None):
        """Create a non-super user"""
        if not email:
            raise ValueError("You must enter an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None):
        """Create and save a superuser with administrator privileges."""
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user