# This util file will help you read the JSON files and provide the JSON data
import json


def get_payload_auth():
    # Read from auth.json and return json
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data


def common_headers():
    headers = {
        "Content-Type": "application/json"
    }
    return headers
