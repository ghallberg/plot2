class Era:
    """Represents a part of the plot, for example a book, an in plot year, or
    any other stretch of time"""
    def __init__(self, name, start = 0, end = -1):
        """ A negaitve number as start or end time represents before or after
        the plots start and end, respectively"""
        if end > 0 and start > end:
            raise ValueError("Era can't end before it starts")
        self.name = name
        self.start = start
        self.end = end

