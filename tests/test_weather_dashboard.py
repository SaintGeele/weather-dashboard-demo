import pytest
from src.weather_dashboard import WeatherDashboard

@pytest.fixture
def dashboard():
    return WeatherDashboard()

def test_fetch_weather(dashboard, mocker):
    mock_response = {
        "main": {"temp": 70, "feels_like": 68, "humidity": 50},
        "weather": [{"description": "clear sky"}]
    }
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: mock_response))
    weather_data = dashboard.fetch_weather("TestCity")
    assert weather_data['main']['temp'] == 70
    assert weather_data['weather'][0]['description'] == "clear sky"

def test_save_to_s3(dashboard, mocker):
    mock_s3 = mocker.patch('boto3.client')
    result = dashboard.save_to_s3({"key": "value"}, "TestCity")
    assert result is True