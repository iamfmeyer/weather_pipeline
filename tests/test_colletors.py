"""Test cases for collectors"""

import pytest
from unittest.mock import Mock, patch
import requests

from src.collectors.dwd_collector import DWDCollector


@pytest.fixture
def dwd_collector():
    """Fixture for DWDCollector"""
    return DWDCollector()


def test_dwd_collector_initialization(dwd_collector):
    """Test collector initialization"""
    assert dwd_collector.base_url == "https://api.brightsky.dev"


@patch("requests.get")
def test_successful_data_collection(mock_get, dwd_collector):
    """Test successful weather data collection"""
    # Mock response
    mock_response = Mock()
    mock_response.json.return_value = {
        "weather": [
            {
                "timestamp": "19-02-2024T12:00:00Z",
                "temperature": 20.5,
                "precipitation": 0.0,
            }
        ]
    }
    mock_get.return_value = mock_response

    # Test data collection
    data = dwd_collector.collect(latitude=51.961563, longitude=7.628202)

    assert "weather" in data
    assert len(data["weather"]) > 0
    assert mock_get.called


@patch("requests.get")
def test_failed_data_collection(mock_get, dwd_collector):
    """Test failed weather data collection"""
    # Setup
    expected_error = "API Error"
    test_lat = 51.961563
    test_lon = 7.628202
    mock_get.side_effect = requests.RequestException(expected_error)

    # Test error handling
    with pytest.raises(requests.RequestException) as exc_info:
        dwd_collector.collect(latitude=test_lat, longitude=test_lon)

    # Asserts
    # 1. Check for correct error message
    assert str(exc_info.value) == expected_error

    # 2. Check if get() was called once
    assert mock_get.call_count == 1

    # 3. Check if get() was called with the correct parameters
    call_args = mock_get.call_args
    assert call_args is not None

    # 4. Check URL and parameters
    url = call_args[0][0]
    params = call_args[1]["params"]

    assert url == f"{dwd_collector.base_url}/weather"
    assert params["lat"] == test_lat
    assert params["lon"] == test_lon
    assert "date" in params
