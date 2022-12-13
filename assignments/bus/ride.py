from datetime import datetime, timedelta


class Ride:
    def __init__(self, ride_id: int, departure_time: datetime.time, arrival_time: datetime.time, driver: str,
                 delays: timedelta.seconds = timedelta(seconds=0)):
        self.ride_id = ride_id
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.driver = driver
        self.delays = delays

    def __str__(self):
        return f"Ride #{self.ride_id}:\n" \
               f"Departure Time: {self.departure_time}\n" \
               f"Operating Driver: {self.driver}\n" \
               f"Expected Delays: {self.delays}\n" \
               f"Arrival Time: {self.arrival_time}"

    def __repr__(self):
        return f"<Ride #{self.ride_id} @ {self.departure_time}>"
