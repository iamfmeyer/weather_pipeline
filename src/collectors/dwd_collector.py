"""DWD Weather Data Collector"""

from datetime import datetime
from typing import Dict, Any, Optional

import requests
from requests.exceptions import RequestException

from .base_collector import BaseCollector


class DWDCollector(BaseCollector):
    """Collector for DWD weather data"""

    def __init__(self) -> None:
        super().__init__()
        self.base_url = "https://api.brightsky.dev"

    def collect(
        self, latitude: float, longitude: float, date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """
        Collect weather data for a specific location from DWD

        Args:
            latitude (float): Location latitude
            longitude (float): Location longitude
            date (Optional[datetime], optional): Optional date for historical data

        Returns:
            Dict[str, Any]: Dict containing weather data

        Raises:
            RequestException: If the API request fails
        """
        try:
            params = {
                "lat": latitude,
                "lon": longitude,
                "date": date.strftime("%d-%m-%Y")
                if date
                else datetime.now().strftime("%d-%m-%Y"),
            }

            self.logger.info(
                f"Collecting weather data for coordinates: {latitude}, {longitude}"
            )

            response = requests.get(f"{self.base_url}/weather", params=params)
            response.raise_for_status()
            data = response.json()

            if self._validate_response(data):
                self.logger.success("Successfully collected weather data")
                return data
            self.logger.warning("Received invalid data format")
            return {}

        except RequestException as e:
            self.logger.error(f"Failed to collect weather data: {str(e)}")
            raise

        def _validate_response(self, data: Dict[str, Any]) -> bool:
            """
            Validate the weather data response

            Args:
                data (Dict[str, Any]): The data to validate

            Returns:
                bool: True if valid, False otherwise
            """
            return bool(data and "weather" in data)
