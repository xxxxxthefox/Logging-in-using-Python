#@xxxxxthefox
import requests

headers = {
    'host': 'bsky.social',
    'content-type': 'application/json',
    'user-agent': 'okhttp/4.12.0',
}

json_data = {
    'identifier': 'User.bsky.social',
    'password': 'password',
    'authFactorToken': '',
    'allowTakendown': True,
}

response = requests.post('https://bsky.social/xrpc/com.atproto.server.createSession', headers=headers, json=json_data)

print(response.status_code)
print(response.text)
