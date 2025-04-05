import requests

def send_line_notification(message, image_path, token):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "message": message
    }
    files = {
        "imageFile": open(image_path, "rb")
    }
    response = requests.post(url, headers=headers, data=data, files=files)
    if response.status_code != 200:
        print("LINE notification failed:", response.text)
    return response.status_code
