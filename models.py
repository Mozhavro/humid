from app import db


class WeatherSnapshot(db.Model):
    """
    Represent a snapshot of a weather stats for a specific time
    and place.
    """
    __tablename__ = 'weather_snapshots'

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer())
    place = db.Column(db.String())
    date = db.Column(db.DateTime())

    def __str__(self):
        return '<WeatherSnapshot id:{id}>'.format(id=self.id)