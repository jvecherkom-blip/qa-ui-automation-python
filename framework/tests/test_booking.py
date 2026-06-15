import pytest
from framework.api.clients.booking_client import BookingClient
from jsonschema import validate
from framework.schemas.booking_schema import booking_schema


client = BookingClient()

schema = {
    "type": "object",
    "properties": {
        "bookingid": {"type": "number"},
        "booking": {"type": "object"}
    },
    "required": ["bookingid", "booking"]
}

def test_create_booking_schema():
    data = {
        "firstname": "Anna",
        "lastname": "Smith",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }

    response = client.create_booking(data).json()

    validate(instance=response, schema=booking_schema)

def test_create_booking(booking_data):
    data = {
        "firstname": "Anna",
        "lastname": "Smith",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }

    response = client.create_booking(booking_data)

    assert response.status_code == 200
    print(response.status_code)
    print(response.json())
    response_data = response.json()
    booking = response_data ["booking"]
    assert booking["firstname"] == booking_data ["firstname"]
    assert booking["lastname"] == booking_data["lastname"]
    assert booking["totalprice"] == booking_data["totalprice"]
    assert booking["depositpaid"] == booking_data["depositpaid"]
    assert booking["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert "bookingid" in response_data
    assert isinstance(response_data["bookingid"], int)


def test_get_booking(booking_data):
    create = client.create_booking(booking_data).json()
    booking_id = create["bookingid"]

    response = client.get_booking(booking_id)

    assert response.status_code == 200

def test_update_booking(auth_token, created_booking):
    
    booking_id = created_booking["bookingid"]

    updated_data = {
  "firstname": "Updated",
  "lastname": "User",
  "totalprice": 123,
  "depositpaid": True,
  "bookingdates": {
      "checkin": "2024-01-01",
      "checkout": "2024-01-05"
  },
  "additionalneeds": "Breakfast"
}

    response = client.update_booking(booking_id, updated_data, auth_token)
    print(response.status_code)
    print(response.text)
    print(response.headers)

    assert response.status_code == 200

def test_delete_booking(auth_token, created_booking):

    booking_id = created_booking["bookingid"]
    response = client.delete_booking(booking_id, auth_token)

    assert response.status_code == 201

def test_get_nonexistent_booking():
    response = client.get_booking(999999)

    assert response.status_code == 404

def test_update_token_wrong():
    response = client.update_booking(1, {}, token="wrong")

    assert response.status_code in [403, 401]

def test_update_booking_without_token(created_booking):
    booking_id = created_booking["bookingid"]

    updated_data = {
        "firstname": "NoAuth",
        "lastname": "User"
    }

    response = client.update_booking(
        booking_id,
        updated_data,
        token=""
    )

    assert response.status_code == 403

def test_update_booking_with_invalid_token(created_booking):
    booking_id = created_booking["bookingid"]

    updated_data = {
        "firstname": "Invalid",
        "lastname": "Token"
    }

    response = client.update_booking(
        booking_id,
        updated_data,
        token="wrongtoken"
    )

    assert response.status_code == 403


@pytest.mark.parametrize(
    "invalid_data, expected_status",
    [
        # ❌ нет firstname → API ведёт себя странно
        (
            {
                "lastname": "Smith",
                "totalprice": 100,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2025-05-01",
                    "checkout": "2025-05-10"
                }
            },
            500  
        ),

        # ❌ неверный тип totalprice
        (
            {
                "firstname": "Anna",
                "lastname": "Smith",
                "totalprice": "one hundred",
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2025-05-01",
                    "checkout": "2025-05-10"
                }
            },
            200
        ),

        # ❌ пустое тело
        ({}, 500)
    ],
    ids=[
        "missing_firstname",
        "invalid_totalprice_type",
        "empty_body"
    ]
)
def test_create_booking_negative(invalid_data, expected_status):
    response = client.create_booking(invalid_data)

    assert response.status_code == expected_status
    if expected_status == 200:
       assert "booking" in response.json()