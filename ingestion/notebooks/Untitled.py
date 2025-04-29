import requests

def send_http_request():
    response = requests.get('https://api.github.com/user')
    return print(response.status_code)

if __name__ == "__main__":
    send_http_request()