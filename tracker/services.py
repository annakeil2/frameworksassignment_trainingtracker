from django.db.models import QuerySet 


def get_total_number_of_training_hours(trainings: QuerySet) -> int:
    """Return the total number of training hours across all trainings."""
    hours = 0
    for training in trainings:
        hours = hours + training.training_hours
    return hours     
              
        
def get_ongoing_training_hours(trainings) -> int:
    """Return the total number of training hours for ongoing trainings."""
    hours = 0
    for training in trainings:
        if training.training_status == training.ONGOING:
            hours = hours + training.training_hours
    return hours        


def get_completed_training_hours(trainings) -> int:
    """Return the total number of training hours for completed trainings."""
    hours = 0
    for training in trainings:
        if training.training_status == training.COMPLETED:
            hours = hours + training.training_hours
    return hours       