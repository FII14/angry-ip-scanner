import requests

url = "http://192.168.1.1/html/login.html"

username = input("Masukkan username: ")
password = input("Masukkan password: ")

data = {
    "username": username,
    "password": password,
}

try:
    response = requests.post(url, data=data)
    if "Login successful" in response.text:
        print("Login berhasil!")
    else:
        print("Login gagal. Username atau password salah.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    
