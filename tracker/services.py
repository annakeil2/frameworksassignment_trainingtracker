from django.db.models import QuerySet 

def get_total_number_of_trainings(trainings: QuerySet) -> int:
    return trainings.count()
        
        
        
def get_number_of_ongoing_trainings(trainings) -> int:
    count = 0
    for training in trainings:
        if training.training_status == training.ONGOING:
            count = count + 1
    return count        

def get_number_of_completed_trainings(trainings) -> int:
    count = 0
    for training in trainings:
        if training.training_status == training.COMPLETED:
            count = count + 1
    return count        