import json

def parse_json(response):

    response = response.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "")

    if response.endswith("```"):
        response = response[:-3]

    return json.loads(response.strip())