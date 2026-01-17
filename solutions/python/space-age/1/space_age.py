def calculate(sec, year):
    res = (sec/31557600) / year
    return res

class SpaceAge:
    sec = 0
    def __init__(self, seconds):
        self.sec = seconds

    def on_mercury(self):
        year = 0.2408467
        return round(calculate(self.sec, year), 2)

    def on_venus(self):
        year = 0.61519726
        return round(calculate(self.sec, year), 2)

    def on_earth(self):
        year = 1.0
        return round(calculate(self.sec, year), 2)

    def on_mars(self):
        year = 1.8808158
        return round(calculate(self.sec, year), 2)

    def on_jupiter(self):
        year = 11.862615
        return round(calculate(self.sec, year), 2)

    def on_saturn(self):
        year = 29.447498
        return round(calculate(self.sec, year), 2)

    def on_uranus(self):
        year = 84.016846
        return round(calculate(self.sec, year), 2)

    def on_neptune(self):
        year = 164.79132
        return round(calculate(self.sec, year), 2)