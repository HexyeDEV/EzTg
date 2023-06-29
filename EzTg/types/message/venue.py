from ..location import Location


class Venue:
    """This object represents a venue.

    Attributes
    ----------
    location: `Location`
        Venue location.
    title: `str`
        Name of the venue.
    address: `str`
        Address of the venue.
    foursquare_id: `str`
        Optional. Foursquare identifier of the venue.
    foursquare_type: `str`
        Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    google_place_id: `str`
        Optional. Google Places identifier of the venue.
    google_place_type: `str`
        Optional. Google Places type of the venue. (See supported types.)
    """

    def __init__(self, data):
        self.location = Location(data["location"])
        self.title = data["title"]
        self.address = data["address"]
        self.foursquare_id = data.get("foursquare_id")
        self.foursquare_type = data.get("foursquare_type")
        self.google_place_id = data.get("google_place_id")
        self.google_place_type = data.get("google_place_type")
