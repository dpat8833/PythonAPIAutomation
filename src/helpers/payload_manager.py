def create_booking_payload():
    payload = {
                "firstname": "123",
                "lastname": "Brown",
                "totalprice": 111,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2023-01-01",
                    "checkout": "2024-01-01",
                },
                "additionalneeds": "Breakfast",
        }
    return payload
