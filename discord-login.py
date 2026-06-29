#@xxxxxthefox
import requests

def login(email, password):
    url = 'https://discord.com/api/v9/auth/login'
    
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36'
    }
    
    payload = {
        "login": email, 
        "password": password, 
        "undelete": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=7)
        print(response.status_code)
        print(response.text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    login("example@gmail.com", "your_password")
