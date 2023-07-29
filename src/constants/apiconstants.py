# Add your constants here
# Adding my URL constants
# Python is all about functions

def base_url():
    return "https://restful-booker.herokuapp.com"

# BASE_URL = "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_update_booking(booking_id):
    return "https://restful-booker.herokuapp.com/" + booking_id
