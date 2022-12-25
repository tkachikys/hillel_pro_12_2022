class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.start = start
        self.end = end
        self.current = self.start

    def increase(self):
        if self.current < 100:
            self.current += 1
        else:
            return "end of count"

    def get_current_value(self):
        print(self.current)


count = DigitalCounter()
count.increase()
count.increase()
count.increase()
count.get_current_value()
