import models

class habits():
    def __init__(self) -> None:
        name = ''
        htype = ''
        duration = 0
    
    def add_habit(self):
        habit = models.habits.objects.create(name=self.name,htype=self.htype,duration=self.duration)
        return "Habit %h : added"%self.name

    def list_habits(self):
        return models.habits.name