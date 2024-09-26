class MyCalendar:

    def __init__(self):
        self.registrations = []

    def book(self, start: int, end: int) -> bool:
        for st, ed in self.registrations:
        # If the present start or end date is actually in between the registration
            if st < end and start <= st:
                return False
            elif start > st and ed > start:
                return False
            elif start <= st and end > ed:
                return False
            elif st <= start and ed > end:
                return False
        self.registrations.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)