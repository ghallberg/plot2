class Relation:
    """Represents a relation between two entities within the plot, can also
    represent awareness, where only certain characters are aware of the others
    (one may be invisible or something)"""
    def __init__(self, name, start, end = -1):
        if end >= 0 and start > end:
            raise ValueError("relation ends end before start")

        self.name = name
        self.start = start
        self.end = end
        self.aware = [] 
        self.participants = []

    def add_participant(self, participant, aware = True):
        self.participants.append(participant)
        if aware:
            self.aware.append(participant)

    def is_aware(self, participant):
        return participant in self.aware

    def is_in(self, participant):
        return participant in self.participants

    def ongoing_at_time(self, time):
        return time > self.start and (self.end < 0 or time < self.end)
