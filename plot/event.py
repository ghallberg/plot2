class Event():
    def __init__(self, name, time, participants = None):
        self.name = name
        self.time = time
        if participants == None:
            self.participants = set() 
        else:
            self.participants = set(participants)


