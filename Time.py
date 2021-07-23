class Time:
    """This class represents time."""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return int_to_time(self.time_to_int() + other.time_to_int())
        
        other += self.time_to_int()
        return int_to_time(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        hour = self.hour == other.hour
        min = self.minute == other.minute
        sec = self.second == other.second

        if hour and min and sec:
            return True

        return False

    def time_to_int(self):
        minute = self.hour * 60 + self.minute
        second = minute * 60 + self.second
        return second

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(intg): # pure function
    time = Time()
    time.hour, time.second = divmod(intg, 3600)
    time.minute, time.second = divmod(time.second, 60)

    return time

