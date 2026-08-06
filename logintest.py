import requests
# Login
login_data = {
    "username": "janedoe",
    "password": "mypassword"
}
response = requests.post("http://localhost:8000/auth/login", json=login_data)
token = response.json()["access_token"]
print(f"Token: {token}")
print(response.json())