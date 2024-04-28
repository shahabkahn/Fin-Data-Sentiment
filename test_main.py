from fastapi.testclient import TestClient
from main import app
from main import TextInput

client = TestClient(app)

def test_positive_sentiment():
    response = client.post("/analyze", json={"text": "Profits are up by 5 million this year."})
    assert response.status_code == 200
    # Ensure that the response is parsed as a list of dictionaries
    data_list = response.json()
    assert isinstance(data_list, list)
    # Check if the first item in the list has a "label" key
    assert data_list[0]["label"] == "positive"

def test_negative_sentiment():
    response = client.post("/analyze", json={"text": "Operating profit totaled EUR 9.4 mn , down from EUR 11.7 mn in 2004 ."})
    assert response.status_code == 200
    # Ensure that the response is parsed as a list of dictionaries
    data_list = response.json()
    assert isinstance(data_list, list)
    # Check if the first item in the list has a "label" key
    assert data_list[0]["label"] == "negative"

def test_neutral_sentiment():
    response = client.post("/analyze", json={"text": "The profits are same as last year"})
    assert response.status_code == 200
    # Ensure that the response is parsed as a list of dictionaries
    data_list = response.json()
    assert isinstance(data_list, list)
    # Check if the first item in the list has a "label" key
    assert data_list[0]["label"] == "neutral"



