import requests


def send_sms_mock(text, recipients):
    # Мокируем API вызов
    print(f"Mocked API call to send SMS with text: {text}, recipients: {recipients}")
    return {"status": "success"}


def send_sms_real(text, recipients):
    # Реальный вызов API (переключение между моком и реальным вызовом)
    api_url = "https://sms4a.de2.retarus.com/rest/v1/jobs"
    payload = {
        "messages": [
            {
                "text": text,
                "recipients": [{"dst": recipient} for recipient in recipients]
            }
        ]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


send_sms = send_sms_mock
