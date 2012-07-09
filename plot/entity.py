class Entity:
    """Represents an Entity in the plot, can be a character, item or even a
    civilization."""
    def __init__(self, name, start = -1, end = -1):
        """Initialize entity parameters:
            name
            start (defaults to -1, any negative number means exists at the beginning of plot)
            end   (defaults to -1, any negative number means exists at the end of plot)
            Raises value error if end is before start.
            """
        if (end > 0 and start > end):
            raise ValueError('End is before start')

        self.name = name
        self.start = start
        self._end = end 

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, time):
        if time <= self.start or self.start == -1:
            self._end = time
        else:
            raise ValueError("end can't be before start")

    def alive_at_time(self, time):
        return time > self.start and (self._end < 0 or time < self._end)
