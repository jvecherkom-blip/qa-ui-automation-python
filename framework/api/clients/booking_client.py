import requests

BASE_URL = "https://restful-booker.herokuapp.com"


class BookingClient:

    def create_token(self, data):
        return requests.post(f"{BASE_URL}/auth", json=data)

    def create_booking(self, data):
        return requests.post(f"{BASE_URL}/booking", json=data)

    def get_booking(self, booking_id):
        return requests.get(f"{BASE_URL}/booking/{booking_id}")

    def update_booking(self, booking_id, data, token):
        headers = {"Cookie": f"token={token}"}
        return requests.put(f"{BASE_URL}/booking/{booking_id}", json=data, headers=headers)

    def delete_booking(self, booking_id, token):
        headers = {"Cookie": f"token={token}"}
        return requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)