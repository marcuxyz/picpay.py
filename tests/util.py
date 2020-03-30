import json

def loadmock(filename: str):
    with open(f"tests/mocks/{filename}", "r") as f:
        return json.loads(f.read())
