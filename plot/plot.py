from entity import Entity
from event import Event
class Plot:
    """Represents the whole plot, keeping track of entities moving betwen
    relations, locations and eras. All times are between 0.0 and 1.0,
    representing the start and end of the plot respectively"""
    def __init__(self, name):
        self.name = name
        self.entities = []
        self.relations = []
        self.events = []

    def entities_at_time(self, time):
        """Return all entities existing at time 'time'"""
        return [ent for ent in self.entities if ent.alive_at_time(time)]

    def relations_at_time(self, time):
        """Return all reltaions ongoing at time 'time'"""
        return [rel for rel in self.relations if ent.ongoing_at_time(time)]

    def get_sorted_events(self):
        return sorted(self.events, key = lambda event: event.time) 

    def add_entity(self, name, **times):
        self.entities.append(Entity(name, **times))

    def has_entity(self, name):
        return len([ent for ent in self.entities if ent.name == name]) > 0

    def _get_entity(self, name):
        if not self.has_entity(name):
            raise ValueError(name + " is not in this plot")

        return [ent for ent in self.entities if ent.name == name][0]

    def entity_alive(self, name, time):
        return self._get_entity(name).alive_at_time(time)

    def edit_entity(self, name, new_name = None, start = None, end = None):
        ent = self._get_entity(name)
        if new_name is not None:
            ent.name = new_name
        if start is not None:
            ent.start = start
        if end is not None:
            ent.end = end

    def add_event(self, name, time, participants = None):
        if participants != None:
            participants = [self._get_entity(part) for part in participants]
        self.events.append(Event(name, time, participants))


