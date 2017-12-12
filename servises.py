import time
import datetime
import random

#TODO use some API
class WeatherService:

    def get_avg_temp_between_dates(self, start, end):
        """
        Provides average temperature for each day between
        start and end dates.
        """
        start_date = datetime.date.fromtimestamp(int(start))
        end_date = datetime.date.fromtimestamp(int(end))
        delta = end_date - start_date

        data = {}
        date = start_date
        for day in range(delta.days):
            timestamp = time.mktime(date.timetuple())
            temperature = self.get_avg_temp_for_day(timestamp)
            data[timestamp] = temperature
            date = date + datetime.timedelta(days=1)

        return data

    def get_avg_temp_for_day(self, timestamp):
        return random.randint(-2, 17)
