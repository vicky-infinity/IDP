import requests

# Signup
signup_data = {
    "name": "Jane Doe",
    "username": "janedoe",
    "email": "jane@example.com",
    "password": "mypassword",
    "confirm_password": "mypassword"
}
response = requests.post("http://localhost:8000/auth/signup", json=signup_data)
print(response.json())
