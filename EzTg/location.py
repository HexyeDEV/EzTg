class Location:
    """Represents a point on the map.
    
    Attributes
    ----------
    longitude: `float`
        Longitude as defined by sender
    latitude: `float`
        Latitude as defined by sender
    horizontal_accuracy: `float`
        Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    live_period: `int`
        Optional. Time relative to the message sending date, during which the location can be updated, in seconds. For active live locations only.
    heading: `int`
        Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
    proximity_alert_radius: `int`
        Optional. Maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    """

    def __init__(self, data):
        self.longitude = data["longitude"]
        self.latitude = data["latitude"]
        self.horizontal_accuracy = data.get("horizontal_accuracy")
        self.live_period = data.get("live_period")
        self.heading = data.get("heading")
        self.proximity_alert_radius = data.get("proximity_alert_radius")