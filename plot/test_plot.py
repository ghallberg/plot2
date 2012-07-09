from unittest import TestCase
from entity import Entity
from era import Era
from event import Event
from location import Location
from relation import Relation
from plot import Plot

class TestPlotBasic(TestCase):
    def setUp(self):
        self.plot = Plot("star wars")

    def test_init(self):
        self.assertTrue(self.plot.name == "star wars")

        self.assertTrue(len(self.plot.entities_at_time(0)) == 0)
        self.assertTrue(len(self.plot.relations_at_time(0)) == 0)

class TestPlotEntities(TestCase):
    def setUp(self):
        self.plot = Plot("star wars")
        self.plot.add_entity("vader")
        self.plot.add_entity("luke")
        self.plot.add_entity("emperor")

    def test_plot_entites(self):

        self.assertTrue(self.plot.has_entity("vader"))
        self.assertTrue(self.plot.entity_alive("vader", 1.0))

        self.plot.edit_entity("vader", end = 0.9)
        self.assertTrue(self.plot.entity_alive("vader", 0.89))
        self.assertFalse(self.plot.entity_alive("vader", 0.9))
        self.assertFalse(self.plot.entity_alive("vader", 0.91))

    def test_plot_events(self):
        self.plot.add_event("duel", 0.9, ["vader", "luke", "emperor"])
        self.plot.add_event("hand loss", 0.5, ["vader", "luke"])

        self.assertTrue(len(self.plot.events) == 2)
        self.assertTrue(self.plot.get_sorted_events()[0].name == "hand loss")

class TestEntity(TestCase):
    def test_init(self):

        ent = Entity("luke")
        self.assertTrue(ent.name == "luke")
        self.assertTrue(ent.start == -1)
        self.assertTrue(ent.end == -1)
        
        ent = Entity("vader", 0, 90)
        self.assertTrue(ent.name == "vader")
        self.assertTrue(ent.start == 0)
        self.assertTrue(ent.end == 90)

        ent = Entity("stormageddon", 60, -1)
        self.assertTrue(ent.name == "stormageddon")
        self.assertTrue(ent.start == 60)
        self.assertTrue(ent.end == -1)

    def test_allowed_endpoints(self):
        self.assertRaises(ValueError, Entity, "lol", 4, 3)


class TestEra(TestCase):
    def test_init(self):
        era = Era("Book1")


class TestEvent(TestCase):
    def test_init(self):
        ev = Event("duel", 90)
        self.assertTrue(ev.name == "duel")
        self.assertTrue(ev.time == 90)


class TestLocation(TestCase):
    def test_init(self):
        loc = Location("the north")


class TestRelation(TestCase):
    def setUp(self):
        self.rel = Relation("parenthood", 0.3, 0.5)

    def test_init(self):
        self.assertTrue(self.rel.name == "parenthood")
        self.assertTrue(len(self.rel.participants) == 0)
        self.assertTrue(len(self.rel.aware) == 0)

    def test_participation(self):
        self.rel.add_participant("vader")
        self.rel.add_participant("luke", False)

        self.assertTrue(self.rel.is_in("vader"))
        self.assertTrue(self.rel.is_in("luke"))
        self.assertTrue(self.rel.is_aware("vader"))
        self.assertFalse(self.rel.is_aware("luke"))
