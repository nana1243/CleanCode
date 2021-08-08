from datetime import timedelta, datetime


class DateRangeIterable:
    """An iterable that contians its own iterator object."""

    def __init__(self,start_date,end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
        current_day += timedelta(days=1)
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration

        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


d = DateRangeIterable(datetime(2020,3,10),datetime(2020,3,20))

print("test2")
for day in (datetime(2020,3,10),datetime(2020,3,20)):
    print(day)

print("test3")

for day in d:
    print(day)